import cv2
import os
import json 
import numpy as np

from tqdm import tqdm

def filter_pic(data):
    output = []
    for obj in data:
        if obj['category'].startswith('lane'):
            output.append(obj)
    return output   

def draw_line(lane_output, data):
    lane_line = [x["poly2d"] for x in data]
    
    for lane in lane_line:
        draw_line = []
        for point in lane:
            temp = point[:2]
            draw_line.append(temp)
        points = np.array(draw_line, np.int32)
        cv2.polylines(lane_output, [points], False, (255,255,255), 2)

    return lane_output

def main(mode="train"):
    val_dir = "/workspace/YOLOP/dataset/det_annotations/val"
    out_dir = "/workspace/YOLOP/dataset/ll_seg_annotations/val"
    
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    val_list = os.listdir(val_dir)

    for val_json in tqdm(val_list):
        val_json = os.path.join(val_dir, val_json)
        val_pd = json.load(open(val_json))
        data = val_pd['frames'][0]['objects']
        img_name = val_pd['name']

        # remain only lane data
        remain = filter_pic(data)
        
        # default black background image
        image_width = 1280
        image_height = 720
        lane_output = np.zeros((image_height, image_width, 3), np.uint8)

        out_path = os.path.join(out_dir, img_name+'.png')
        if remain:
            lane_output = draw_line(lane_output, remain)
                
        cv2.imwrite(out_path, lane_output)
    else:
        pass

if __name__ == '__main__':
    main(mode='train')
