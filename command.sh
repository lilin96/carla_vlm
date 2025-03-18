# create conda env
conda create -y -n vlm-rl python=3.8
conda activate vlm-rl

conda install pytorch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 pytorch-cuda=12.1 -c pytorch -c nvidia
pip install -r requirements.txt
MAX_JOBS=4 pip install flash-attn==2.3.6 --no-build-isolation

# Download Carla
mkdir /home/users/ntu/songyanz/scratch/carla
cd /home/users/ntu/songyanz/scratch/carla
wget https://carla-releases.s3.us-east-005.backblazeb2.com/Linux/CARLA_0.9.13.tar.gz
tar -xf CARLA_0.9.13.tar.gz

# Download Internvl Model
mkdir /home/users/ntu/songyanz/scratch/pretrained/Mini-InternVL2-4B-DA-DriveLM
# local terminal
rsync -avz /home/lin/proj/VLM-RL/internvl_chat/pretrained/Mini-InternVL2-4B-DA-DriveLM.zip songyanz@aspire2antu.nscc.sg:/home/users/ntu/songyanz/scratch/pretrained/Mini-InternVL2-4B-DA-DriveLM
# on server
cd /home/users/ntu/songyanz/scratch/pretrained/Mini-InternVL2-4B-DA-DriveLM
unzip Mini-InternVL2-4B-DA-DriveLM.zip