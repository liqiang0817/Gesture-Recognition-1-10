import sys
import os
import time
caffe_root = '/home/lq/caffe-ssd/' 
sys.path.append(caffe_root + 'python')
import caffe
import cv2
import numpy as np

caffemodel = '/home/lq/caffe-ssd/my-caffe-project/gesture_recognition/snapshot/gesture_recognition__iter_60000.caffemodel'
deploy = '/home/lq/caffe-ssd/my-caffe-project/caffe-code-master/prototxt/ResNet_50_deploy.prototxt'
#testfile = '/home/sy/Stamp/sku/'
caffe.set_mode_gpu()
#test = 'YP1000040/YP1000040_3_0_1_1_1_1_1_1.jpg'
net = caffe.Net(deploy, caffemodel, caffe.TEST)
mean = np.ones([3,224,224], dtype = np.float)
mean[0,:,:] = 104.
mean[1,:,:] = 117.
mean[2,:,:] = 123.

def getCategory(imagepath):
	img = caffe.io.load_image(imagepath)
	transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
	transformer.set_transpose('data', (2,0,1))
	transformer.set_raw_scale('data',255)

	transformer.set_channel_swap('data', (2,1,0))

	net.blobs['data'].data[...] = transformer.preprocess('data', img)

	net.blobs['data'].data[0][0,:,:] -= mean[0,:,:]
	net.blobs['data'].data[0][1,:,:] -= mean[1,:,:]
	net.blobs['data'].data[0][2,:,:] -= mean[2,:,:]

	#	start = time.time()
	out = net.forward()
        #print out
	#out = net.predict([img])
	#predicts = out.argmax()
	#print predicts
	#	end = time.time()

	#category = net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]
	category = net.blobs['prob'].data[0].argmax()
	#print category
	return category

total = 0
accuracycount = 0 
labdic = {}
labels = np.loadtxt('/home/lq/caffe-ssd/my-caffe-project/test_filelist.txt', str, delimiter = '\t')
for label in labels:
	if labdic.has_key(label.split(' ')[1]):
		continue
	else:
		labdic[label.split(' ')[1]] = label.split(' ')[0]
#imagepath = '/home/lq/caffe-ssd/my-caffe-project/gesture_recognition/test/3/00001.jpg'
imgdir = '/home/lq/caffe-ssd/my-caffe-project/gesture_recognition/test/3/'
for imgname in os.listdir(imgdir):
    imagepath = imgdir + imgname
    predict = getCategory(imagepath)
    print str(int(predict)+1)
#for files in os.listdir(testfile):
	#filepath = testfile + files + '/':
		#total += 1
		#print total
		#imagepath = filepath + image
		#predict = getCategory(imagepath)
		#print 'true class:',files[7:9]
		#print 'predict class:',labdic[str(predict)][7:9]
		#if files[7:9] == labdic[str(predict)][7:9]:
			#accuracycount += 1
#print float(accuracycount)/total
#net = caffe.Classifier(deploy, caffemodel, channel_swap= (2,1,0),raw_scale = 255)
#for num in range(1,42):
#    if len(str(num)) == 1:
#		num = '0' + str(num)
#    else:
#        num = str(num)
#    print num
	#img = caffe.io.load_image('/home/sy/Stamp/sku/YP10000{0}/YP10000{1}.jpg'.format(num,num))

#labels = np.loadtxt('/home/sy/Stamp/valList.txt', str, delimiter = '\t')
    #print 'YP10000{0}:'.format(num)
#for label in labels:
#    if label[7:9] == '40':
#		print label.split(' ')[1]
#		break
#for i in np.arange(category.size):
#	print category[i]
#    print '\n'
