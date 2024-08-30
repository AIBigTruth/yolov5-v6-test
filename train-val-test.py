import os
import random
import shutil


def moveFile(input1, input2, save1, save2, picknumber):
    pathDir = os.listdir(input1)  # 取图片的原始路径
    random.seed(1)
    filenumber = len(pathDir)  # 原文件个数
    sample = random.sample(pathDir, picknumber)  # 随机选取需要数量的样本图片
    print("out:", sample)
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
    train_img = 'G:/github/test/firesmoke-train-images-4000'
    train_txt = 'G:/github/test/firesmoke-train-txt-4000'
    val_img = 'G:/github/test/val-images'
    val_txt = 'G:/github/test/val-txt'
    test_img = 'G:/github/test/test-images'
    test_txt = 'G:/github/test/test-txt'
    # val
    if not os.path.exists(val_txt):
        os.makedirs(val_txt)
    if not os.path.exists(val_img):
        os.makedirs(val_img)
    moveFile(train_img, train_txt, val_img, val_txt, 800)
    # test
    if not os.path.exists(test_txt):
        os.makedirs(test_txt)
    if not os.path.exists(test_img):
        os.makedirs(test_img)
    moveFile(train_img, train_txt, test_img, test_txt, 800)