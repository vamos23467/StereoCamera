#===============================
#カメラ提示システムコード
# Raspi4 conect to two USBCam
#
#===============================
# -*- coding: utf-8 -*-
import cv2
import time
 #https://qiita.com/fujioka244kogacity/items/0b739464bb81f089cded
#-------------------------------
# Webカメラ
#-------------------------------
WIDTH =   640
HEIGHT =  480
FPS =   30

def cam_set(DEVICE_ID,WIDTH,HEIGHT,FPS):
    # video capture
    cap = cv2.VideoCapture(DEVICE_ID)

    # フォーマット・解像度・FPSの設定
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, FPS)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    
    cv2.namedWindow('screen',cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('screen',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)                                                         

    # フォーマット・解像度・FPSの取得
    fourcc = decode_fourcc(cap.get(cv2.CAP_PROP_FOURCC))
#     width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
#     height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)
#     print("ID:{} fourcc:{} fps:{}　width:{}　height:{}".format(DEVICE_ID, fourcc, fps, width, height))

    return cap

def decode_fourcc(v):
        v = int(v)
        return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])

def main():
    #--------------------------------------
    DEVICE_ID = "/dev/video0"
    cap1=cam_set(DEVICE_ID,WIDTH,HEIGHT,FPS)

    DEVICE_ID = "/dev/video2"
    cap2=cam_set(DEVICE_ID,WIDTH,HEIGHT,FPS)

    while True:
        
        # カメラ画像取得
        _, frame1 = cap1.read()
        time.sleep(0.01)
        frame1 = cv2.resize(frame1, dsize=(960, 1080))
        if(frame1 is None):
            continue

        # カメラ画像取得
        _, frame2 = cap2.read()
        time.sleep(0.01)
        frame2 = cv2.resize(frame2, dsize=(960, 1080))
        if(frame2 is None):
            continue

        im_h=cv2.hconcat([frame1,frame2])

        #---------------------------
        # 画像表示
        cv2.imshow(None,im_h)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # VideoCaptureオブジェクト破棄
    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()

#-------------------------------
if __name__ == '__main__':
    main()
