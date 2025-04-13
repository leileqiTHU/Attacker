from config import *
from openai import OpenAI
from templates import attacker_template
from utils import save_jsonl
import re
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

client = OpenAI(api_key="EMPTY", base_url=f"http://localhost:{ATTACKER_PORT}/v1")

def get_attacker_completion(prompt, k):
    completion = client.completions.create(
        model=ATTACKER_MODEL,
        prompt=prompt,
        n=k,
        max_tokens=768,
    )
    return [choice.text for choice in completion.choices]

def extract_queries(completions):
    pattern = r"<query>(.*?)</query>"
    return [re.search(pattern, c, re.DOTALL).group(1).strip() if re.search(pattern, c, re.DOTALL) else "" for c in completions]

def process_single_question(question):
    prompt = attacker_template.format(question=question)
    completions = get_attacker_completion(prompt, K)
    queries = extract_queries(completions)
    return dict(question=question, prompt=prompt, completions=completions, queries=queries)

def generate_queries(dataset):
    questions = dataset['prompt']
    results = []

    with ThreadPoolExecutor() as executor:
        results = list(tqdm(executor.map(process_single_question, questions), total=len(questions), desc="Generating Attacks (map)"))

    save_jsonl(ATTACK_FILE_PATH, results)
    return results
