import json
from pycocoevalcap.bleu.bleu import Bleu
from pycocoevalcap.rouge.rouge import Rouge
from pycocoevalcap.cider.cider import Cider
references = {}
hypothesis = {}
j=0
# Open .jsonl file
with open("/your_path/Caption_result.jsonl", mode="r", encoding="utf-8") as file:
    # 按行读取文件
    for line in file:
        j = j + 1
        # 解析每行的 JSON 数据
        data = json.loads(line.strip())
        label=data['label']
        predict=data['predict']
        references[j - 1] = [label]
        hypothesis[j - 1] = [predict]

# Compute each evaluation metric
# BLEU
bleu_scorer = Bleu(4)
bleu_score, bleu_scores = bleu_scorer.compute_score(references, hypothesis)
print("BLEU Scores:", bleu_score)

# ROUGE
rouge_scorer = Rouge()
rouge_score, rouge_scores = rouge_scorer.compute_score(references, hypothesis)
print("ROUGE Score:", rouge_score)

# CIDEr
cider_scorer = Cider()
cider_score, cider_scores = cider_scorer.compute_score(references, hypothesis)
print("CIDEr Score:", cider_score)