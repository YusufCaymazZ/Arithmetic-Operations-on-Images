import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

class imageBlending:
    def __init__(self,path1,path2,add1,add2,y):
        self.path1 = path1
        self.path2 = path2
        self.add1 = add1
        self.add2 = add2
        self.y = y
    def blending(self):
        pass


    def changepat1(self,path):
        self.path1 = path
    
    def changepat2(self,path):
        self.path2 = path

    def changeadd1(self,add):
        self.add1 = add

    def changeadd2(self,add):
        self.add2 = add

    def changey(self,y):
        self.y = y