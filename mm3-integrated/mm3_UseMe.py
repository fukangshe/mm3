# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 11:53:58 2021

@author: Fukan
"""
import os
from PyQt5 import QtWidgets
import sys
import subprocess
import shlex
import re

os.chdir(os.path.dirname(os.path.realpath(__file__)))

class wid(QtWidgets.QWidget):
    def __init__(self):
        super(wid, self).__init__()
        grid=QtWidgets.QGridLayout()
        grid.setSpacing(5)
        
        grid.addWidget(QtWidgets.QLabel('please input the directory of yaml file'),1,1)
        self.yaml_path = QtWidgets.QLineEdit(self)
        grid.addWidget(self.yaml_path,1,3)
        
        self.runbtn = QtWidgets.QPushButton('curate',self)
        grid.addWidget(self.runbtn,2,3)
        self.runbtn.setCheckable(True)
        self.runbtn.clicked.connect(self.curate)
        grid.addWidget(QtWidgets.QLabel('step 1:'),2,2)
        
        self.runbtn = QtWidgets.QPushButton('compile',self)
        grid.addWidget(self.runbtn,3,3)
        self.runbtn.setCheckable(True)
        self.runbtn.clicked.connect(self.compile0)
        grid.addWidget(QtWidgets.QLabel('step 2:'),3,2)
        
        self.runbtn = QtWidgets.QPushButton('channel_picker',self)
        grid.addWidget(self.runbtn,4,3)
        self.runbtn.setCheckable(True)
        self.runbtn.clicked.connect(self.channel_picker)
        grid.addWidget(QtWidgets.QLabel('step 3:'),4,2)
        
        self.runbtn = QtWidgets.QPushButton('subtract',self)
        grid.addWidget(self.runbtn,5,3)
        self.runbtn.setCheckable(True)
        self.runbtn.clicked.connect(self.subtract)
        grid.addWidget(QtWidgets.QLabel('step 4:'),5,2)
        
        self.runbtn = QtWidgets.QPushButton('segment',self)
        grid.addWidget(self.runbtn,6,3)
        self.runbtn.setCheckable(True)
        self.runbtn.clicked.connect(self.segment)
        grid.addWidget(QtWidgets.QLabel('step 5:'),6,2)
        
        self.setLayout(grid)
        self.setWindowTitle('mother machine data process')
        self.show()
        
    def curate(self):
        yaml=str(self.yaml_path.text()).strip()
        s='python.exe'+' mm3_metamorphToTIFF.py'+' -f '+yaml
        arg=shlex.split(s)
        sub=subprocess.Popen(arg,stdout=subprocess.PIPE,stderr=STDOUT)
        stdout = sub.communicate()[0]
        print(stdout)
        print(sub.poll())
        
    def compile0(self):
        yaml=str(self.yaml_path.text()).strip()
        s='python.exe'+' mm3_Compile.py'+' -f '+yaml
        arg=shlex.split(s)
        sub=subprocess.Popen(arg,stdout=subprocess.PIPE)
        b_stdout= sub.communicate()[0]
        stdout=b_stdout.decode('utf-8')
        stdout=re.sub('.\x08','',stdout,count=25)
        print(stdout)
        print(sub.poll())
        
    def channel_picker(self):
        yaml=str(self.yaml_path.text()).strip()
        s='python.exe'+' mm3_ChannelPicker.py'+' -f '+yaml
        arg=shlex.split(s)
        sub=subprocess.Popen(arg,stdout=subprocess.PIPE)
        b_stdout= sub.communicate()[0]
        stdout=b_stdout.decode('utf-8')
        stdout=re.sub('.\x08','',stdout,count=25)
        print(stdout)
        print(sub.poll())
        
    def subtract(self):
        yaml=str(self.yaml_path.text()).strip()
        s='python.exe'+' mm3_Subtract.py'+' -f '+yaml
        arg=shlex.split(s)
        sub=subprocess.Popen(arg,stdout=subprocess.PIPE)
        b_stdout= sub.communicate()[0]
        stdout=b_stdout.decode('utf-8')
        stdout=re.sub('.\x08','',stdout,count=25)
        print(stdout)
        print(sub.poll())
        
    def segment(self):
        yaml=str(self.yaml_path.text()).strip()
        s='python.exe'+' mm3_Segment-Unet.py'+' -f '+yaml
        arg=shlex.split(s)
        sub=subprocess.Popen(arg,stdout=subprocess.PIPE)
        b_stdout= sub.communicate()[0]
        stdout=b_stdout.decode('utf-8')
        stdout=re.sub('.\x08','',stdout,count=25)
        print(stdout)
        print(sub.poll())
        
    def shutdown(self):
        print('GUI exited')
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = wid()
    ret = app.exec_()
    ex.shutdown()
    sys.exit(ret)

if __name__ == '__main__':
    main()       