import cv2
import numpy as np

import json
import os

from argparse import ArgumentParser as ArgParse

# Color palette for lane visualization
def getcolor(code):
    if code == 1:
        return (0, 255, 0)
    if code == 2:
        return (0, 255, 255)
    if code == 3:
        return (255, 255, 0)
    if code == 4:
        return (255, 0, 0)
    if code == 5:
        return (0, 0, 255)
    if code == 6:
        return (45, 88, 200)
    if code == 7:
        return (213, 22, 224)

def process(root_dir, json_file):
    
    # Image visualization
    cv2.namedWindow("image", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("image",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    count = 1

    # Open lane and class ground truth files
    with open(root_dir + json_file, 'r') as file, open(root_dir + json_file.replace('.json','_classes.txt'), 'r') as classes:
        json_lines = file.readlines()
        class_lines = classes.readlines()
        line_index = 0

        # Iterate over each image
        while line_index < len(json_lines):
            json_line = json_lines[line_index]
            class_line = class_lines[line_index]
            i = 0
            sample = json.loads(json_line)
            class_line = class_line.strip()
            class_list = class_line.split(' ')
            lanes = sample['lanes']
            raw_file = root_dir + sample['raw_file']

            # Display image and draw lane
            while i < len(lanes):
                im = cv2.imread(raw_file)
                polyline = []
                for v in range(0, len(sample['h_samples']) - 1):

                    point_h_begin = sample['h_samples'][v]
                    point_h_end = sample['h_samples'][v + 1]
                    point_w_begin = lanes[i][v]
                    point_w_end = lanes[i][v + 1]

                    if(point_w_begin != -2 and point_w_end != -2):
                        cv2.circle(im, (point_w_begin, point_h_begin), 3, getcolor(int(class_list[i])))

                cv2.putText(im,'continuous yellow',(0,40), cv2.FONT_HERSHEY_SIMPLEX, 1,getcolor(1),2,cv2.LINE_AA)
                cv2.putText(im,'continuous',(0,70), cv2.FONT_HERSHEY_SIMPLEX, 1,getcolor(2),2,cv2.LINE_AA)
                cv2.putText(im,'dashed',(0,100), cv2.FONT_HERSHEY_SIMPLEX, 1,getcolor(3),2,cv2.LINE_AA)
                cv2.putText(im,'double-dashed',(0,130), cv2.FONT_HERSHEY_SIMPLEX, 1,getcolor(4),2,cv2.LINE_AA)
                cv2.putText(im,'Botts\' dots',(0,170), cv2.FONT_HERSHEY_SIMPLEX, 1,getcolor(5),2,cv2.LINE_AA)
                cv2.putText(im,'double continuous',(0,200), cv2.FONT_HERSHEY_SIMPLEX, 1,getcolor(6),2,cv2.LINE_AA)
                cv2.putText(im,'unknown',(0,230), cv2.FONT_HERSHEY_SIMPLEX, 1,getcolor(7),2,cv2.LINE_AA)
                cv2.putText(im,'Count: ' + str(count),(400,40), cv2.FONT_HERSHEY_SIMPLEX, 1,getcolor(7),2,cv2.LINE_AA)
                cv2.imshow('image', im)

                code = cv2.waitKey(0)
                i+=1

                # Code for navigation
                # If z is pressed exit from the program
                if code == ord('z'):
                    #closeall(output, file)
                    return
                if code == ord('l'):
                    line_index += 100
                    count += 100
                    break                
                if code == ord('k'):
                    line_index += 50
                    count += 50
                    break                
                if code == ord('j'):
                    line_index += 20
                    count += 20
                    break
                if code == ord('h'):
                    line_index += 10
                    count += 10
                    break
            count += 1
            line_index += 1

if __name__=='__main__':
    ap = ArgParse()
    ap.add_argument('--root', type=str, default='.')
    ap.add_argument('--labels', type=str, default='label_data_0313.json')

    args = ap.parse_args()

    process(args.root, args.labels)
