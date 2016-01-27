from pylab import plot, show, title, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
from scipy.io.wavfile import read,write

def getPeak(y,Fs):
    n = len(y) # lungime semnal
    k = arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    rq = frq[range(int(n/2))] # one side frequency range

    Y = fft(y)/n # fft computing and normalization
    Y = Y[range(int(n/2))]

    fr = 0
    mag = 0
    for i in range(2500,3000):
        if abs(Y[i]) > mag:
            fr = i
            mag = abs(Y[i])
    return fr

Fs = 44100;  # sampling rate


cold = 7
rate,data=read('7c_water.wav')
y=data[:,1]

cold_f = getPeak(y,Fs)

hot = 100
rate,data=read('hot_water.wav')                                                                             
y=data[:,1] 

hot_f = getPeak(y,Fs)

rate,data=read('test_12C.wav')
y=data[:,1]
x = getPeak(y,Fs)
m = (cold-hot)/(cold_f-hot_f)
y = -m*x + (-m*-hot_f) + cold

print(y)



