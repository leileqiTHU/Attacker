from pathlib import Path

# Basic Configs
K = 10 #ASR@K
BATCH_SIZE = 200
SCORE_WITH_QUESTION = True

# Models and Ports
ATTACKER_MODEL = 'Attacker-v0.1'
ATTACKER_PORT = 8001

TARGET_MODEL = 'Llama-2-7b-chat-hf/'
TARGET_PORT = 8000

TARGET_MODEL = 'gemma-2-9b-it/'
TARGET_PORT = 8003

TARGET_MODEL = 'Qwen2.5-7B-Instruct/'
TARGET_PORT = 8004

TARGET_MODEL = 'Mistral-7B-Instruct-v0.3/'
TARGET_PORT = 8005

TARGET_MODEL = 'Llama-3.1-8B-Instruct/'
TARGET_PORT = 8006

TARGET_MODEL = 'gpt-4o-mini'

target_model_name = Path(TARGET_MODEL).stem

EVAL_MODEL = 'HarmBench-Llama-2-13b-cls/'
EVAL_PORT = 8002

# dataset and slice
DATASET_PATH = "./harmbench_standard_trl_standard_format"
DATA_SLICE = slice(0, 200)  

# output file paths
BASE_NAME = f"attacker_on_HarmBench-v6-510steps_@{K}_{DATA_SLICE.start}-{DATA_SLICE.stop}"
ATTACK_FILE_PATH = f"./outputs/{BASE_NAME}_attack_prompt.jsonl"
RESPONSE_FILE_PATH = f"./outputs/{target_model_name}/{BASE_NAME}/attack_prompt_with_target_response.jsonl"
RESPONSE_SCORED_PATH = (
    f"./outputs/{target_model_name}/{BASE_NAME}/HarmbenchCls_score-with-question.jsonl"
    if SCORE_WITH_QUESTION else
    f"./outputs/{target_model_name}/{BASE_NAME}/HarmbenchCls_score-with-query.jsonl"
)

SHOW_PLOTS = True

SYSTEM_PROMPT = "You are a helpful assistant."