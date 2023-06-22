# -*- coding: utf-8 -*-
"""
Created on Fri May  5 18:41:06 2023

@author: mustafa
"""

import pydirectinput
import time
from PIL import ImageGrab
from PIL import Image
from numpy import asarray
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

time.sleep(1)


while True:
    try: 
        '''
        imagehp = ImageGrab.grab(bbox=(350, 250, 475,260))
        imagehp.save('hp.png')
        hp = pytesseract.image_to_string(r'hp.png')
        hp=hp.replace(" ", "")
        hp=hp.replace("\n", "")
        hp = hp[0:3]
        hp = int(hp)
        '''
        imagemp = ImageGrab.grab(bbox=(350, 60, 440,92))
        imagemp.save('mp.png')
        mp = pytesseract.image_to_string(r'mp.png')
        mp=mp.replace(" ", "")
        mp=mp.replace("\n", "")
        mp = mp[0:4]
        mp = int(mp)
        

        
        if mp < 2750:    
            pydirectinput.press('2')
        '''

        if hp < 515:
            pydirectinput.press('1')
        '''
    except:
        print('hata')
