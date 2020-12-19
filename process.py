# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'process.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#
# Subscribe to PyShine Youtube channel for more detail! 

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
from cv2 import cv2
import imutils

class Ui_MainWindow(object):

	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(652, 541)
		
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setObjectName("label")
		self.horizontalLayout.addWidget(self.label)
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setObjectName("label_2")
		self.verticalLayout_2.addWidget(self.label_2)
		self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
		self.verticalSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
		self.verticalSlider.setObjectName("verticalSlider")
		self.verticalLayout_2.addWidget(self.verticalSlider)
		self.horizontalLayout.addLayout(self.verticalLayout_2)
		self.verticalLayout_3 = QtWidgets.QVBoxLayout()
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setObjectName("label_3")
		self.verticalLayout_3.addWidget(self.label_3)
		self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
		self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
		self.verticalSlider_2.setObjectName("verticalSlider_2")
		self.verticalLayout_3.addWidget(self.verticalSlider_2)
		self.horizontalLayout.addLayout(self.verticalLayout_3)
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_3.setObjectName("pushButton_3")
		self.verticalLayout.addWidget(self.pushButton_3)
		self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_4.setObjectName("pushButton_4")
		self.verticalLayout.addWidget(self.pushButton_4)
		self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_5.setObjectName("pushButton_5")
		self.verticalLayout.addWidget(self.pushButton_5)
		self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_6.setObjectName("pushButton_6")
		self.verticalLayout.addWidget(self.pushButton_6)
		self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_7.setObjectName("pushButton_7")
		self.verticalLayout.addWidget(self.pushButton_7)
		self.horizontalLayout.addLayout(self.verticalLayout)
		self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setObjectName("pushButton")
		self.horizontalLayout_2.addWidget(self.pushButton)
		self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_2.setObjectName("pushButton_2")
		self.horizontalLayout_2.addWidget(self.pushButton_2)
		spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_2.addItem(spacerItem1)
		self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		self.verticalSlider.valueChanged['int'].connect(self.brightness_value)
		self.verticalSlider_2.valueChanged['int'].connect(self.blur_value)
		self.pushButton.clicked.connect(self.loadImage)
		self.pushButton_2.clicked.connect(self.savePhoto)
		self.pushButton_3.clicked.connect(self.hist)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Görüntü İşleme Projesi"))
		self.label.setText(_translate("MainWindow", "Görüntü"))
		self.pushButton_3.setText(_translate("MainWindow", "Histogram"))
		self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
		self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
		self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
		self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
		self.pushButton.setText(_translate("MainWindow", "Open"))
		self.pushButton_2.setText(_translate("MainWindow", "Save"))


		# Added code here
		self.filename = None # Will hold the image address location
		self.tmp = None # Will hold the temporary image for display
		self.brightness_value_now = 0 # Updated brightness value
		self.blur_value_now = 0 # Updated blur value

	def loadImage(self):
		""" This function will load the user selected image
			and set it to label using the setPhoto function
		"""
		self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
		if(self.filename):
			self.image = cv2.imread(self.filename)
			self.setPhoto(self.image)


	def setPhoto(self,image):
		""" This function will take image input and resize it 
			only for display purpose and convert it to QImage
			to set at the label.
		"""
		self.tmp = image
		image = imutils.resize(image,width=320)
		frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
		self.label.setPixmap(QtGui.QPixmap.fromImage(image))

	def savePhoto(self):
		""" This function will save the image"""

		filename = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]
		if(filename):
			cv2.imwrite(filename,self.tmp)
			print('Image saved as:',self.filename)

	def brightness_value(self,value):
		""" This function will take value from the slider
			for the brightness from 0 to 99
		"""
		self.brightness_value_now = value
		print('Brightness: ',value)
		self.update()
		
	def blur_value(self,value):
		""" This function will take value from the slider 
			for the blur from 0 to 99 """
		self.blur_value_now = value
		print('Blur: ',value)
		self.update()

	def update(self):
		""" This function will update the photo according to the 
			current values of blur and brightness and set it to photo label.
		"""
		img = self.changeBrightness(self.image, self.brightness_value_now)
		img = self.changeBlur(img,self.blur_value_now)
		self.setPhoto(img)

	def changeBrightness(self,img,value):
		""" This function will take an image (img) and the brightness
			value. It will perform the brightness change using OpenCv
			and after split, will merge the img and return it.
		"""
		hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		h,s,v = cv2.split(hsv)
		lim = 255 - value
		v[v>lim] = 255
		v[v<=lim] += value
		final_hsv = cv2.merge((h,s,v))
		img = cv2.cvtColor(final_hsv,cv2.COLOR_HSV2BGR)
		return img
		
	def changeBlur(self,img,value):
		""" This function will take the img image and blur values as inputs.
			After perform blur operation using opencv function, it returns 
			the image img.
		"""
		kernel_size = (value+1,value+1) # +1 is to avoid 0
		img = cv2.blur(img,kernel_size)
		return img

	def hist(self):
		img = cv2.cvtColor(self.tmp, cv2.COLOR_RGB2GRAY)
		img_hist = cv2.equalizeHist(img)
		self.setPhoto(img_hist)

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())