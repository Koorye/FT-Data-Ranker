# FT-Data-Ranker
FT-Data-Ranker比赛方案。

## 方案
1. refine，采用alpaca-cot的refine方案对数据集进行细化。
2. minhash，对相似度大于0.7的文档进行去重。
3. 按比例采样中英文，50%中文、50%英文。

## 如何使用
0. 预先准备好预训练模型
1. 将原始数据放在data/raw目录下，分别命名为raw_data_en.jsonl/raw_data_zh.jsonl。
2. 调用`./process_data/process_data.sh`进行处理。
3. 调用`python process_data/get_train_dataset_1b.py`进行采样，将输出名为"test_1b.jsonl"的数据集。
4. 训练模型
```
./lm-training/train_scripts/deepspeed_train_1b.sh \
<your_model_path> \
test_1b.jsonl \
<output_path>
```
