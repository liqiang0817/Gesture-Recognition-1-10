#!/usr/bin/env sh
# -*- coding:utf-8 -*-
# This script test four voc images using faster rcnn end-to-end trained model (ZF-Model)
set -e
#从if到fi，其作用是判断选用哪一个gpu
if [ ! -n "$1" ] ;then
    #如果该shell是带参数的，而且其第一个参数"$1"是非空的，-n是判断一个判断式，后面的字符串非空则返回非零；空则返回0.通过前面的否定表达式！，[ ! -n "$1" ]的意思是，如果不带参数，则gpu=0
    echo "\$1 is empty, default is 0"
    gpu=0
else
    echo "use $1-th gpu"
    gpu=$1
fi


CAFFE=/home/lq/caffe-ssd/build/tools/caffe
#其默认的目录是caffe-reid目录，MODEL下有train.proto等文件
MODEL=/home/lq/caffe-ssd/my-caffe-project/gesture_recognition/model

#下面由GLOG_log_dir开始的一长串是用来指定输出日志的位置的。后面接的是$CAFFE train，这是一个caffe的命令，用于开始模型的训练，该命令后面的均是train的参数。
#gpu参数
#solve的位置
#weights表示已有模型，说明此时的训练是在已有模型上进行finetuning
GLOG_log_dir=$MODEL $CAFFE train \
    --gpu $gpu \
    --solver /home/lq/caffe-ssd/my-caffe-project/caffe-code-master/prototxt/resnet50_solver.prototxt \
    --weights /home/lq/caffe-ssd/my-caffe-project/gesture_recognition/ResNet-50-model.caffemodel
    #--snapshot /home/sy/Stamp/snapshot/resnet__iter_375000.solverstate
