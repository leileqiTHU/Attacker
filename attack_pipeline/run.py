from datasets import load_from_disk
from config import *
from attack import generate_queries
from response import generate_responses
from score import score_responses
from evaluate import evaluate
from utils import load_jsonl
import argparse

def main(stage):
    dataset = load_from_disk(DATASET_PATH)
    dataset = dataset.select(range(*DATA_SLICE.indices(len(dataset))))

    if stage == 'attack':
        generate_queries(dataset)
    elif stage == 'respond':
        data = load_jsonl(ATTACK_FILE_PATH)
        generate_responses(data)
        score_responses()
        evaluate()
    elif stage == 'score':
        score_responses()
        evaluate()
    elif stage == 'all':
        data = generate_queries(dataset)
        data = generate_responses(data)
        score_responses()
        evaluate()
    elif stage == 'eval':
        evaluate()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--stage', choices=['attack', 'respond', 'score', 'all', 'eval'], default='all')
    args = parser.parse_args()
    main(args.stage)
