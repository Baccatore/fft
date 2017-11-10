#coding: utf-8
# Fast Fourier Transform Script
# Author: Yuichiro SUGA
# Created: 2017-11-03
# Updated: 2017-11-10

import numpy as np
import csv
import matplotlib.pyplot as plt
import sys

fileName = ''   # File Name as Input in ./inputCSV
data = []       # Data list in time space
sp = []         # Spectrum in frequency space
freq = []       # Frequency axis
N = 1024        # Number of input data in time space
dt = 2.00E-07   # Time step
#headValue = 0  # First value of input CSV file
                # This value is used for validation that
                # the program successfully to read from
                # the first line of the input CSV file

def preamble():
    print('FFT program')
    print('Created on 2017-11-03')
    print('By Yuichiro SUGA @ Doshisha Univ.')

def readFile():
    global fileName
    fileName = sys.argv[1]

def analysis():
    global data, sp, freq, date, fileName
    with open('./inputCSV/'+fileName) as dataFile:
        rows = csv.reader(dataFile, delimiter=',',
                quotechar='|')
        for i in range(20):     # Change value if the first line 
                                # to read changes
            next(rows)
        for row in rows:    
            data.append(row[0]) # Change value if the culumn to
                                # read changes
        sp = np.fft.fft(data[0:N])
        freq = np.fft.fftfreq(N,d=dt)

def output():
    global data,  sp, freq, fileName
    #Select the range without DC component 
    freq = freq[1:N>>1]
    sp = list(map(abs,sp[1:N>>1]))
    #CSV output
    with open('./outputCSV/'+fileName[0:-4]+ 'FFT.CSV','w') as csvfile:
        writer = csv.writer(csvfile, 
                delimiter=',',
                quotechar='|',
                quoting=csv.QUOTE_NONNUMERIC,
                lineterminator='\n')
        writer.writerow(['Frequency[Hz]','Amplitude(Abs)'])
        for i in range((N>>1)-1):
            record = [freq[i],sp[i]]
            writer.writerow(record)
    #Graph output
    plt.xlabel('x: Frequenciy [Hz]')
    plt.ylabel('y: Amplitude [V]')
    plt.title(fileName)
    plt.plot(freq,sp)
    plt.savefig('./outputFigure/'+fileName[0:-3]+'png')
    plt.show() #Uncomment if you wanna show the graph
    #Standard output for logging
    print(fileName)

# For the use without the shell script
def prologue():
    print('Thank you ! Bye:)')
    print('--END of Program--\n')

if __name__ == '__main__':
    #preamble()
    readFile()
    analysis()
    output()
    #prologue()

