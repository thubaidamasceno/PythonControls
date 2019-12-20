import numpy as np

##In order to import this toolbox into a python script you need to 
##do the following. Copy the following lines of code below
# import sys
# sys.path.append('/home/carlos/Dropbox/BlackBox/plotting')
# from plotting import *

# or

# In order to get python to search for all of your lovely blackbox 
# python routines. Add this to your .bashrc file

# for d in /home/carlos/Dropbox/BlackBox/*/; do
# 	PYTHONPATH+=:$d
# done
# export PYTHONPATH

# For Thonny make symbolic links here
# ~/.thonny/BundledPython36/lib/python3.6/site-packages$ 

def dlmread(filename,delimiter=',',suppressWarnings=False,variableLength=0):

    try:
        file_ID = open(filename)
    except:
        if suppressWarnings == False:
            print(filename,"Does Not Exist")
        return None;
    
    if 1: ##Wha? Why is this here? ***facepalm***
        print("Successfully Opened File = ",filename)
        data = []
        ctr = -1
        for line in file_ID:
            ctr+=1
            #Ok so if the delimiter is a space sometimes fortran is wierd and has a ton of spaces
            #so we need something more robust -- so for FORTRAN we will add a try catch statement below
            row = line.split(delimiter)
            row_np = []
            for x in row:
                try:
                    val = np.float(x)
                    row_np.append(val)
                except:
                    val = []
                    #print 'x=',x
            # if len(row_np) != 35:
            #     print 'line=',line
            #     print 'row =',row
            #     print 'row_np=',row_np,len(row_np)
            if len(row_np) > 0:
                if (variableLength != 0):
                        while len(row_np) != variableLength:
                            #Pad vector with zeros
                            row_np.append(0)
                #print row_np,len(row_np)
                data.append(np.asarray(row_np))
            
        data_np = np.asarray(data)
        print('(Rows,Cols) = ',np.shape(data_np))
        return data_np

# Copyright - Carlos Montalvo 2017
# You may freely distribute this file but please keep my name in here
# as the original owner
