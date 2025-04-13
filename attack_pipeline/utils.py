import json
from pathlib import Path

def save_jsonl(path, data):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as f:
        for item in data:
            f.write(json.dumps(item) + '\n')

def load_jsonl(path):
    with open(path, 'r') as f:
        return [json.loads(line) for line in f]
