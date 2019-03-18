'''
This code aims to transform xml format to txt.
It contains class and bounding box information (x_min, x_max, y_min, y_max).
The New format: 
              classname1(One-hot) x_center y_center width height
              classname2(One-hot) x_center y_center width height
              ...
              classnamen(One-hot) x_center y_center width height
Sth important: all of that were normalized in [0, 1]
'''

import os
import xml.etree.ElementTree as ET

def xml_2_txt(xml_dir):
    # a+ mode to open txt_file
    # f = open(txt_path, 'a+')
    filelists = os.listdir(xml_dir)
    for file in filelists:
        file_path = xml_dir + '/' + str(file)
        # open this_name.txt
        txt_path = xml_dir + '/' + 'labels/' + file[:-3] + 'txt'
        f = open(txt_path, 'a+')

        # read xml's information
        in_file = open(file_path)
        tree = ET.parse(in_file)

        # Got image original path
        path = tree.findtext('path')
        print(path)

        for img_size in tree.iter('size'):
            width = img_size.findtext('width')
            height = img_size.findtext('height')
        print(width, height)

        # iter object (It looks like different obj will output with sort.)
        for obj in tree.iter('object'):
            xml_class = obj.findtext('name')
            print(xml_class)

            xml_box = obj.find('bndbox')
            x_min = float(xml_box.findtext('xmin'))
            x_max = float(xml_box.findtext('xmax'))
            y_min = float(xml_box.findtext('ymin'))
            y_max = float(xml_box.findtext('ymax'))
            print(x_min, x_max, y_min, y_max)

            if xml_class == 'Naruto':
                class_OneHot = '0'
            elif xml_class == 'Jiraiya':
                class_OneHot = '1'
            print(class_OneHot)

            x_center = (x_max+x_min)/(2*float(width))
            y_center = (y_max+y_min)/(2*float(height))
            final_width = (x_max-x_min)/float(width)
            final_height = (y_max-y_min)/float(height)

            content = class_OneHot + ' ' + str(x_center) + ' ' + str(y_center) + ' ' + str(final_width)\
                      + ' ' + str(final_height) + '\n'
            f.write(content)

# Input your xml files path.
xml_2_txt('C:/Users/Gsx/Desktop/xml')
