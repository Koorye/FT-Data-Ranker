#!/bin/bash

python process_data.py --config configs/en/refine.yaml
python process_data.py --config configs/zh/refine.yaml

python process_data.py --config configs/en/minhash.yaml
python process_data.py --config configs/zh/minhash.yaml
