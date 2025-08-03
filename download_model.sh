#!/bin/bash

cd /workspace/tripo/TripoSR
mkdir -p ckpts
wget https://huggingface.co/VAST-AI/TripoSR/resolve/main/ckpts/uvit_v2.pth -O ckpts/uvit_v2.pth
