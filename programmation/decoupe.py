import cv2

imgs = [cv2.imread(f"output/{i}.png") for i in range(1,577)]

imgs_h = [cv2.hconcat(imgs[24*i:24*(i+1)]) for i in range(24)]
img = cv2.vconcat(imgs_h)
cv2.imshow("test.png", img)
cv2.waitKey()
cv2.imwrite("flag_decoupe.png", img)
