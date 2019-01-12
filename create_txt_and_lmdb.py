# -*- coding: UTF-8 -*-
import subprocess
import os
import re


def createFileList(images_path, txt_save_path):
     #打开图片列表清单txt文件 
     fw = open(txt_save_path,"w") 
     #查看图片目录下的文件,相当于shell指令ls 
     images_name = os.listdir(images_path)
     #遍历所有文件名 
     for file in images_name:
          gesture = os.listdir(images_path+file)
          for eachname in gesture:
          #正则表达式这里可以根据情况进行更改 
          #正则表达式规则:找0开头,紧跟0到9999四个数字，并以jpg结尾的图片文件
               pattern_img = r'(^0\d{0,9999}.jpg$)'
          #正则表达式匹配 
               img_name = re.search(pattern_img, eachname)
          #按照规则将内容写入txt文件中 
               if img_name != None:
                    fw.write('train224'+'/'+file+'/'+img_name.group(0) +' '+str(int(file)-1)+'\n')
               #打印成功信息
     print("生成txt成功")
     #关闭fw
     fw.close()


if __name__ == '__main__': 
     #caffe_root目录 
     caffe_root = '/home/lq/caffe-ssd/' 
     #my-caffe-project目录 
     my_caffe_project = caffe_root + 'my-caffe-project/' 
     #图片存放目录 
     images_path = my_caffe_project + 'gesture_recognition/train224/'
     #生成的图片列表清单txt文件名 
     txt_name = 'train_filelist.txt'
     #生成的图片列表清单txt文件的保存目录 
     txt_save_path = my_caffe_project + txt_name
     #生成txt文件 
     createFileList(images_path, txt_save_path)


# def create_db(caffe_root, images_path, txt_save_path):
#      #lmdb文件名字
#      lmdb_name = 'img_train.lmdb'
#      print('1')
#      #生成的db文件的保存目录
#      lmdb_save_path = caffe_root + 'my-caffe-project/' + lmdb_name
#      print('2')
#      #convert_imageset工具路径
#      convert_imageset_path = caffe_root + 'build/tools/convert_imageset'
#      print('3')
#      cmd = """%s --shuffle --resize_height=256 --resize_width=256 %s %s %s"""
#      print('4')
#      status, output = subprocess.getstatusoutput(cmd % (convert_imageset_path, images_path,txt_save_path, lmdb_save_path))
#      print('5')
#      print(output)
#      if(status == 0):
#           print("lmdb文件生成成功")
#
#
# if __name__ == '__main__':
#      #caffe_root目录
#      caffe_root = '/home/lq/caffe-ssd/'
#      #my-caffe-project目录
#      my_caffe_project = caffe_root + 'my-caffe-project/'
#      #图片存放目录
#      images_path = my_caffe_project + 'gesture-recognition/train/'
#      #生成的图片列表清单txt文件名
#      txt_name = 'train_filelist.txt'
#      #生成的图片列表清单txt文件的保存目录
#      txt_save_path = my_caffe_project + txt_name
#      #生成txt文件
#      createFileList(images_path, txt_save_path)
#      #生成lmdb文件
#      create_db(caffe_root, images_path, txt_save_path)
