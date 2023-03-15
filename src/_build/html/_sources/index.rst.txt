.. figure_read documentation master file, created by
   sphinx-quickstart on Fri Nov 11 15:37:28 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to figure_read's documentation!
=======================================
This module read the tagged figure and export the data as csv file. The axis is tagged using pure green color. The data point is tagged using pure red color. The figure can be tagged using Paint(Windows) and KolourPaint(Linux). The opencv-python package is required to execute the program.

To install the software, please add the following line to ~/.bashrc and source ~/.bashrc again.

.. code-block:: console
	
	source $HOME/Figure_Read/src/etc/bashrc
	
To execute the program, please save the tagged figure as figure.png. Execute the program by typing the following command. x1 and x2 are the range of x-axis. y1 and y2 are the range of y-axis. The extracted result will be generated as result.csv

.. code-block:: console
	
	figure_read x1 x2 y1 y2

.. toctree::
   data
   figure_read
   



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
