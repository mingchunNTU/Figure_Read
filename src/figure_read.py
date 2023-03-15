import numpy as np
import cv2
from data import *

def axis_transform(pixel,pixel_range,axis_range): 
	"""
	Transform the pixel position to physical value
	
	:param pixel: pixel position
	:type pixel: float
	:param pixel_range: the pixel position of the two ends of axis
	:type pixel_range: list
	:param axis_range: the corresponding physical value of the two ends of axis
	:type axis_range: list
	"""
	output=axis_range[0]*(pixel_range[1]-pixel)/(pixel_range[1]-pixel_range[0])+axis_range[1]*(pixel-pixel_range[0])/(pixel_range[1]-pixel_range[0])
	return output

def figure_read(fig,xrange,yrange):    
	"""
	Read the tagged figure and export the data in variable format
	
	:param fig: tagged figure
	:type fig: string
	:param xrange: range of x-axis of the tagged data
	:type xrange: list
	:param yrange: range of y-axis of the tagged data
	:type yrange: list
	:return: list of two variables that contain x coordinate and y coordinate respectively
	:rtype: list
	
	"""

	# read in the figure
	img=cv2.imread(fig)
	size=img.shape    
	# read in the axis range
	axes=[]
	for i in range(size[1]):
		for j in range(size[0]):
			if img[j,i,0]==0 and img[j,i,1]==255 and img[j,i,2]==0:
				axes.append([j,i])   
  
	# read in the data point
	data=[]
	for i in range(size[1]):
		for j in range(size[0]):
			if img[j,i,0]==0 and img[j,i,1]==0 and img[j,i,2]==255:
				data.append([j,i])    
	x_coordinate=variable("x coordinate","-",[])
	y_coordinate=variable("y coordinate","-",[])
	x1=axes[1][1] # the x coordinate of the second point
	x2=axes[2][1] # the x coordinate of the third point
	y1=axes[1][0] # the y coordinate of the second point
	y2=axes[0][0] # the y coordinate of the first point
	for i in data:	
		tmp1=axis_transform(i[1],[x1,x2],xrange)
		tmp2=axis_transform(i[0],[y1,y2],yrange)
		x_coordinate.value.append(tmp1)
		y_coordinate.value.append(tmp2)
	output=[x_coordinate,y_coordinate]       
	return output

