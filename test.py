#! /usr/bin/python


import subprocess as sp
import numpy
import os 
import shlex
import signal
import time
import gc
import datetime
import sys
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import urllib2
import json
import ctypes
import io

temp = "test"
i=0
w = 928
h = 616
nbytes = w*h*3
raw_image = 0
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",14)

while True:
	ibytes = io.BytesIO()
	raw_image = sys.stdin.read(nbytes)
	i = i + 1
	if ( i % 5 == 0 ):
		req = urllib2.Request('http://localhost:4316/api/controller/live/text', headers={'User-Agent' : "Magic Browser"}) 
		response = urllib2.urlopen(req)
		data = json.load(response)   
		for slide in data['results']['slides']:
			if slide['selected'] == True:
				temp = slide['text']

			
	img = Image.frombuffer('RGB', (w,h), raw_image, 'raw', 'RGB', 0, 1)
	draw=ImageDraw.Draw(img)
	draw.text((0, 460), temp ,(255,255,0),font=font)
	draw.text((580, 460), str(i) ,(255,255,0),font=font)
	img.save(ibytes, format="JPEG", subsamling=0, quality=100)
	sys.stdout.write(ibytes.getvalue())
	
