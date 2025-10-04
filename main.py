try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from pySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance

import maya.OpenMayaUI  as omui

ROOT_RESOURCE_DIR = 'C:/Users/ICT68/Documents/maya/2025/scripts/myStyleTool/resources'

class MyStyleToolDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setWindowTitle("My Tool UI")
		self.resize(300,80)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet('background-color: #F2C6C2; color: #593939')

		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/Images/Pink_Triangle.png")
		scaled_pixmap = self.imagePixmap.scaled(
			QtCore.QSize(100,100),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation
		)
		self.imageLabel.setPixmap(scaled_pixmap)
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)

		self.mainLayout.addWidget(self.imageLabel)

		self.nameLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.nameLayout)

		self.nameIconLabel = QtWidgets.QLabel()
		self.nameIconPixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/Icons/cube.png")
		cube_scaled_pixmap = self.nameIconPixmap.scaled(
			QtCore.QSize(16,16),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation
		)

		self.nameIconLabel.setPixmap(cube_scaled_pixmap)
		
		self.nameLayout.addWidget(self.nameIconLabel)

		self.nameLabel = QtWidgets.QLabel("Name :")
		self.nameLabel.setStyleSheet(
			'''
			QLabel {
				color: #593939;
				font-family: Comic Sans MS;
				font-size: 14px;
				font-weight: bold;
			}
			'''
		)
		

		self.nameLineEdit = QtWidgets.QLineEdit()
		self.nameLineEdit.setStyleSheet(
			'''
			QLineEdit {
				border: 1px solid #BF5E5E;
				border-radius: 10px;
				color: #BF5E5E;
				font-family: Comic Sans MS;
				font-size: 12px;
			}
			'''
		)
		self.nameLayout.addWidget(self.nameLabel)
		self.nameLayout.addWidget(self.nameLineEdit)
		
		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)
		self.createButton = QtWidgets.QPushButton("Create")
		self.createButton.setStyleSheet(
			'''
			QPushButton {
				background-color: #F2DBD5;
				color: #593939;
				border: 2px solid #593939;
				border-radius: 5px;
				font-size: 14px;
				font-family: Comic Sans MS;
				font-weight: bold;
				font-style: italic;
				padding: 8px;
			}
			QPushButton:hover {
				background-color: qlineargradient(x1:0, y1:0,x2:0,y2:1,stop:0 #F4EEED,stop:1 #F2DBD5);
			}
			QPushButton:pressed {
				background-color: #D9B2A9
			}
			'''
			)
		self.cancelButton = QtWidgets.QPushButton("Cancel")
		self.cancelButton.setStyleSheet(
			'''
			QPushButton {
				background-color: #F2DBD5;
				color: #593939;
				border: 2px solid #593939;
				border-radius: 5px;
				font-size: 14px;
				font-family: Comic Sans MS;
				font-weight: bold;
				font-style: italic;
				padding: 8px;
			}
			QPushButton:hover {
				background-color: qlineargradient(x1:0, y1:0,x2:0,y2:1,stop:0 #F4EEED,stop:1 #F2DBD5);
			}
			QPushButton:pressed {
				background-color: #D9B2A9
			}
			'''
			)
		self.cancelButton.clicked.connect(self.close)
		self.buttonLayout.addWidget(self.createButton)
		self.buttonLayout.addWidget(self.cancelButton)

		self.mainLayout.addStretch()

def run():
	global ui

	try:
		ui.close()
	except:
		pass

	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.QWidget)
	ui = MyStyleToolDialog(parent=ptr)
	ui.show()