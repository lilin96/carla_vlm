import argparse
import json
import os

from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm

FOOT = ImageFont.truetype('/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf', 50)


def custom_image(input_data, image_size=448):
    captions = ['cam_front_left', 'cam_front', 'cam_front_right', 'cam_back_left', 'cam_back', 'cam_back_right']
    # captions = ['CAM_FRONT_LEFT', 'CAM_FRONT', 'CAM_FRONT_RIGHT', 'CAM_BACK_LEFT', 'CAM_BACK', 'CAM_BACK_RIGHT']

    width = image_size * 2
    height = image_size
    # count = 0
    imgs = {}
    for caption in captions:
        img = Image.fromarray(input_data[caption][0])
        # old_wide, old_height = img.size
        img = img.resize((width, height))
        if img.mode != "RGB":
            img = img.convert("RGB")
            
        draw = ImageDraw.Draw(img)
        text = caption
        draw.text((0, 0), text, fill=(255, 0, 255), font=FOOT)
        imgs[caption] = img

    result_width = width * 3
    result_height = height * 2
    result_img = Image.new('RGB', (result_width, result_height))
    imgs = [imgs[caption] for caption in captions]

    for i in range(len(imgs)):
        row = i // 3
        col = i % 3

        left = col * width
        top = row * height
        right = left + width
        bottom = top + height
        result_img.paste(imgs[i], (left, top))
       
    # result_path = os.path.join(save_path,'.jpg')
    # result_img.save(result_path)
    return result_img


def get_images(ann_file):
    with open(ann_file, 'r') as f:  # , \
        train_file = json.load(f)

    images = {}
    for scene_id in train_file.keys():
        scene_data = train_file[scene_id]['key_frames']
        for frame_id in scene_data.keys():
            image_id = scene_id + '_' + frame_id
            if image_id not in images:
                images[image_id] = scene_data[frame_id]['image_paths']
            else:
                print(image_id)

    return images


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-root', type=str, default='InternVL-Domain-Adaptation-Data/images/drivelm')
    parser.add_argument('--ann-file', type=str, default='InternVL-Domain-Adaptation-Data/v1_1_train_nus.json')
    args = parser.parse_args()
    images = get_images(args.ann_file)
    save_path = os.path.join(args.data_root, 'stitch')
    os.makedirs(save_path, exist_ok=True)
    custom_image(img_paths=images, save_path=save_path)
