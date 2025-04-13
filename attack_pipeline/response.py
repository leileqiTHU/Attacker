from config import *
from openai import OpenAI
from utils import load_jsonl, save_jsonl
from openai_api import get_openai_res
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

client = OpenAI(api_key="EMPTY", base_url=f"http://localhost:{TARGET_PORT}/v1")


def get_target_completion(prompt):
    try:
        
        if 'gemma' in TARGET_MODEL.lower():
            msgs = [
            # {"role": "system", "content": SYSTEM_PROMPT}, #gemma does not support system prompt
            {"role": "user", "content": prompt}
            ]
        
        else:
            msgs = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]

        if 'gpt' in TARGET_MODEL.lower():
            return get_openai_res(msgs, model_name = TARGET_MODEL)
        completion = client.chat.completions.create(
            messages=msgs,
            model=TARGET_MODEL,
            max_tokens=768
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"[Error] Target model failed for input: {prompt[:50]}... | {e}")
        return None

def process_item(item):
    responses = [get_target_completion(q) for q in item['queries']]
    item['target_responses'] = responses
    return item

def generate_responses(data):
    with ThreadPoolExecutor() as executor:
        results = list(tqdm(executor.map(process_item, data), total=len(data), desc="Generating Responses (target model)"))

    save_jsonl(RESPONSE_FILE_PATH, results)
    return results
