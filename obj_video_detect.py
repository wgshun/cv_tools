# !/usr/sbin/env python
# coding = utf-8
#
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import _init_paths

import os
import time

from opts import opts
from detectors.detector_factory import detector_factory

class ImageProcess(object):
    def __init__(self):
        opt = opts().init()
        os.environ['CUDA_VISIBLE_DEVICES'] = '0'
        opt.debug = max(opt.debug, 1)
        Detector = detector_factory[opt.task]
        self.detector = Detector(opt)
        self.vca_class_name = ['aeroplane']

    def run(self, img):
        t0 = time.time()
        
        ret = self.detector.run(img)
        results = ret['result']
        result = []
        for i in results:
            ymin = int(i[1])
            xmin = int(i[0])
            ymax = int(i[3])
            xmax = int(i[2])
            score = float(i[4])
            label = self.vca_class_name[int(i[5])-1]
            result.append([label, score, xmin, ymin, xmax, ymax])

        t1 = time.time()
        print('The object recognition time :', str(t1-t0))
        return result


# import cv2
# img_detector = ImageProcess()
# img = cv2.imread('dog.jpg')
# print(img_detector.run(img))
