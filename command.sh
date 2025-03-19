# create conda env
conda create -y -n vlm-rl python=3.8
conda activate vlm-rl

conda install pytorch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 pytorch-cuda=12.1 -c pytorch -c nvidia

pip install -r requirements.txt
pip install -r requirements/internvl_chat.txt
MAX_JOBS=4 pip install flash-attn==2.3.6 --no-build-isolation

qsub  -I -l select=1:ncpus=16:ompthreads=1:mem=50GB -P personal-songyanz -l walltime=01:00:00

module load cuda/12.2.2
module load git