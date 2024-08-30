import os
import random
import shutil


def moveFile(input1, input2, save1, save2, picknumber):
    pathDir = os.listdir(input1)  # 取图片的原始路径
    random.seed(1)
    filenumber = len(pathDir)  # 原文件个数
    sample = random.sample(pathDir, picknumber)  # 随机选取需要数量的样本图片
    print("val:", sample)
    list_len = len(sample)
    print(list_len)
    list = []
    for i in range(len(sample)):
        list.append(sample[i].split('.')[0])
    print("name:", list)
    for flie_name in list:
        path_img = os.path.join(input1, flie_name + '.jpg')
        shutil.move(path_img, save1)
        path_lab = os.path.join(input2, flie_name + '.txt')
        shutil.move(path_lab, save2)


if __name__ == '__main__':
    train_img = 'G:/github/yolov5-v6/dataset/firesmoke-5000-v1/images/train2024-firesmoke-5000-v1'
    train_txt = 'G:/github/yolov5-v6/dataset/firesmoke-5000-v1/labels/train2024-firesmoke-5000-v1'
    val_img = 'G:/github/yolov5-v6/dataset/firesmoke-5000-v1/images/val2024-firesmoke-500-v1'
    val_txt = 'G:/github/yolov5-v6/dataset/firesmoke-5000-v1/labels/val2024-firesmoke-500-v1'
    if not os.path.exists(val_txt):
        os.makedirs(val_txt)
    if not os.path.exists(val_img):
        os.makedirs(val_img)
    moveFile(train_img, train_txt, val_img, val_txt, 500)