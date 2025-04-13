from config import *
from harmbench_cls_util import HarmBenchScorer
from utils import load_jsonl, save_jsonl
from tqdm import tqdm

def score_responses():
    scorer = HarmBenchScorer(model_id=EVAL_MODEL, model_port=EVAL_PORT)
    data = load_jsonl(RESPONSE_FILE_PATH)

    for item in tqdm(data):
        item['if_unsafes'] = []
        for i, resp in enumerate(item['target_responses']):
            score_res = scorer.score(
                query=item['question'] if SCORE_WITH_QUESTION else item['queries'][i],
                response=resp[:2000]
            )
            item['if_unsafes'].append(score_res['score'])

    save_jsonl(RESPONSE_SCORED_PATH, data)
    return data
