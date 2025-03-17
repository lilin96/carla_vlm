# create conda env
conda create -y -n vlm-rl python=3.9
conda activate vlm-rl

conda install pytorch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 pytorch-cuda=12.1 -c pytorch -c nvidia

pip install -r requirements.txt
pip install -r requirements/internvl_chat.txt
MAX_JOBS=4 pip install flash-attn==2.3.6 --no-build-isolation