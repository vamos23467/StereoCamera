#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import time

#===============================
# カメラ提示システムコード
# Raspi4 connected to two USB Cams
#===============================

#-------------------------------
# Webカメラ設定
#-------------------------------
WIDTH = 640
HEIGHT = 480
FPS = 30

def cam_set(device_id, width, height, fps):
    cap = cv2.VideoCapture(device_id)
    
    # フォーマット・解像度・FPSの設定
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cap.set(cv2.CAP_PROP_FPS, fps)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    
    cv2.namedWindow('screen', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('screen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    return cap

def decode_fourcc(v):
    v = int(v)
    return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])

def main():
    #--------------------------------------
    device_id1 = "/dev/video0"
    device_id2 = "/dev/video2"
    
    cap1 = cam_set(device_id1, WIDTH, HEIGHT, FPS)
    cap2 = cam_set(device_id2, WIDTH, HEIGHT, FPS)

    while True:
        # カメラ画像取得
        ret1, frame1 = cap1.read()
        if not ret1 or frame1 is None:
            continue

        ret2, frame2 = cap2.read()
        if not ret2 or frame2 is None:
            continue
        
        frame1 = cv2.resize(frame1, (960, 1080))
        frame2 = cv2.resize(frame2, (960, 1080))

        im_h = cv2.hconcat([frame1, frame2])

        # 画像表示
        cv2.imshow('screen', im_h)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # VideoCaptureオブジェクト破棄
    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
