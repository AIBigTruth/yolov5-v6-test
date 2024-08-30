import glob
import os

# labelImg软件打标签后xml转为yolv5训练的txt格式，转化过程中进行了归一化操作

xml_in_path = 'G:/github/yolov5-v6/dataset/firesmoke-4000-v2/images/firesmoke-xml-4453/'
txt_out_path = 'G:/github/yolov5-v6/dataset/firesmoke-4000-v2/images/firesmoke-txt-4453/'

def _read_anno(filename):
    import xml.etree.ElementTree as ET
    tree = ET.parse(filename)
    size = tree.find('size')
    w, h = [int(float(size.find('width').text)),
           int(float(size.find('height').text))]

    objects = []
    if w == 0:
        return []
    for obj in tree.findall('object'):
        name = obj.find('name').text
        if name == 'fire':
            label = 0
        else:
            label = 1

        if label != 1:
            #读取检测框的左上、右下角点的坐标
            bbox = obj.find('bndbox')
            x1, y1, x2, y2 = [int(bbox.find('xmin').text),
                              int(bbox.find('ymin').text),
                              int(bbox.find('xmax').text),
                              int(bbox.find('ymax').text)]
            #这里也很关键，yolov5需要中心点以及宽和高的标注信息，并且进行归一化，下边label后边的四个值即是归一化后保留4位有效数字的x，y，w，h
            obj_struct = [label, round((x1+x2)/(2.0*w), 4), round((y1+y2)/(2.0*h), 4), round((x2-x1)/(w), 4), round((y2-y1)/(h), 4)]
            objects.append(obj_struct)
    return objects

if __name__ == '__main__':
    t = ''
    #获取所有的xml文件路径
    allfilepath = []
    for file in os.listdir(xml_in_path):
        if file.endswith('.xml'):
            file = os.path.join(xml_in_path, file)
            allfilepath.append(file)
        else:
            pass
    #生成需要的对应xml文件名的txt
    print("allfilepath:", allfilepath)
    empty_num = 0
    for file in allfilepath:
        name = file.split('.')[0]
        name2 = name.split('/')[-1]
        result = _read_anno(file)
        out_path = txt_out_path + name2 + '.txt'
        if len(result)==0:
            fp = open(out_path, 'w+')
            fp.close()
            print("empty: ", file)
            empty_num = empty_num + 1

        else:
            with open(out_path,'w') as f:
                for line in result:
                    for a in line:
                        t = t+str(a)+' '
                    f.writelines(t)
                    f.writelines('\n')
                    t =''
    print("empty_num: ", empty_num)
