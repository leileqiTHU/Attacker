# Attacker-v0.1-RedTeam-Pipeline

---
A modular and configurable pipeline for generating adversarial prompts to evaluate LLM safety using Attacker-v0.1.

## 🚀 Features

- Modular 3-stage pipeline: `Attack ➝ Response ➝ Score`
- Easily configurable (models, ports, dataset, slice)
- Resume from any stage (load intermediate files)
- Batch processing and multithreading
- Automatic ASR@K evaluation
- Optional result visualization

---

## 🛠️ Setup

```bash
pip install -r requirements.txt
```

Ensure you have:
- VLLM servers running for attacker, target, and eval models
- Dataset at path specified in `config.py`

---

## ⚙️ Configuration

Edit `harmbench_attack_pipeline/config.py` to modify:
- `K`, batch size, dataset range
- `Attacker/target/eval models and ports
- Output paths and scoring options

---

## 🔄 Pipeline Usage
### First, deploy your models
```bash
# Target Models
CUDA_VISIBLE_DEVICES=0 vllm serve Llama-2-7b-chat-hf/ --port 8000
CUDA_VISIBLE_DEVICES=2 vllm serve gemma-2-9b-it/ --port 8003
CUDA_VISIBLE_DEVICES=3 vllm serve Qwen2.5-7B-Instruct/ --port 8004
CUDA_VISIBLE_DEVICES=4 vllm serve Mistral-7B-Instruct-v0.3/ --port 8005
CUDA_VISIBLE_DEVICES=5 vllm serve Llama-3.1-8B-Instruct/ --port 8006
# Evaluation models
CUDA_VISIBLE_DEVICES=1 vllm serve HarmBench-Llama-2-13b-cls/ --port 8002
# Attacker-v0.1
CUDA_VISIBLE_DEVICES=6,7 vllm serve Attacker-v0.1/ --port 8001
```
modify the model paths and ports

### Then, run the pipeline
```bash
# Run all stages (attack ➝ respond ➝ score ➝ show_results)
python -m attack_pipeline.run --stage all

# Run from saved attacker outputs
python -m attack_pipeline.run --stage respond

# Run from saved attacker outputs
python -m attack_pipeline.run --stage score

# Evaluate ASR@K and visualize
python -m attack_pipeline.run --stage eval
```

---

## 📊 Outputs

- Intermediate results saved in `outputs/`
- Final CSV with ASR@K in same folder
- Optional plot shows ASR@1 to ASR@K

---

## 🧩 Customization

Want to:
- Use other models or scoring logic?

→ plug in your own scoring logic inside `score.py`.


## 📝 License

- License: Research Use Only
- Usage Restrictions: This model is intended for research purposes only. For commercial use or other inquiries, please contact the model author.


## Citation

If you use this model in your research or work, please cite it as follows:

```
@misc{leqi2025Attacker,
  author = {Leqi Lei},
  title = {The Safety Mirage: Reinforcement-Learned Jailbreaks Bypass Even the
Most Aligned LLMs},
  year = {2025},
  howpublished = {\url{URL_to_model_repository}},
  note = {Accessed: 2025-04-13}
}
```