coco_path = 'coco_dataset/coco_val2017/val2017'
annotation_file = 'coco_dataset/coco_val2017/instances_val2017.json'
save_path = 'coco_val'

import json
import os
import cv2

if not os.path.exists(save_path):
    os.mkdir(save_path)

dataset = json.load(open(annotation_file, 'r'))

anns, cats, imgs = {}, {}, {}
if 'annotations' in dataset:
    for ann in dataset['annotations']:
        anns[ann['id']] = ann

if 'images' in dataset:
    for img in dataset['images']:
        imgs[img['id']] = img

if 'categories' in dataset:
    for cat in dataset['categories']:
        cats[cat['id']] = cat

for img in imgs.keys():
    image = cv2.imread(os.path.join(coco_path,imgs[img]['file_name']))
    if image is not None:
        for ann in anns.keys():
            if anns[ann]['image_id'] == img:
                # print(anns[ann]['bbox'], cats[anns[ann]['category_id']]['name'])
                # print(os.path.join(coco_path, imgs[img]['file_name']))

                image_bbox = anns[ann]['bbox']
                image_name = cats[anns[ann]['category_id']]['name']
                cv2.putText(image, image_name, (int(image_bbox[0]-10), int(image_bbox[1]-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 1)
                cv2.rectangle(image, (int(image_bbox[0]), int(image_bbox[1])), (int(image_bbox[0]+image_bbox[2]), int(image_bbox[1]+image_bbox[3])), (0, 255, 0), 1)
    else:
        print(imgs[img]['file_name'])
    cv2.imwrite(os.path.join(save_path, imgs[img]['file_name']), image)
    # break
