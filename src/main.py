from figure_read import *
from data import *
import sys

fig="figure.png"

x1=float(sys.argv[1])
x2=float(sys.argv[2])
y1=float(sys.argv[3])
y2=float(sys.argv[4])


output=figure_read(fig,[x1,x2],[y1,y2])

file='./result.csv'
variable_output(output,file)
