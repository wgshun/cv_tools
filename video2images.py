import argparse
import os
import sys
import cv2

class video_process(object):
    def __init__(self, args):
        self.frame_gap = args.frame_gap
        self.video_file = args.video_file
        self.save_path = args.save_path
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)
        self.process(self.video_file)
        print('Video to images, over.')

    def process(self, video_url):

        cap = cv2.VideoCapture(video_url)
        if cap.isOpened():
            video_name = os.path.basename(video_url).split('.')[0]
            save_path = os.path.join(self.save_path, video_name)
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            frame_id = 0
            ret_img, img = cap.read()

            while ret_img and img is not None:
                if self.frame_gap > 1 and 0 != frame_id % self.frame_gap:
                    ret_img, img = cap.read()
                    frame_id += 1
                    continue
                frame_id += 1
                cur_img_file = os.path.join(save_path,'{}.jpg'.format(frame_id))
                cv2.imwrite(cur_img_file, img)
                cv2.imshow('frame', img)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            cap.release()

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_file', type=str,
                        help='视频文件', default='1.mp4')
    parser.add_argument('--frame_gap', type=int,
                        help='图片间隔帧数', default=10)
    parser.add_argument('--save_path', type=str,
                        help='图片保存路径', default='result')
    return parser.parse_args(argv)


if __name__ == '__main__':
    vp = video_process(parse_arguments(sys.argv[1:]))
