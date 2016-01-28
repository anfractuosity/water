from pylab import plot, show, title, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
from scipy.io.wavfile import read,write

Fs = 48000

def window(y):

    inc = int(len(y)/10)
    ps = 0
    c = 0
    for i in range(0,len(y),inc):
        hot_f = getPeak(y[i:i+inc],Fs)
        if hot_f > 0:
            ps = ps + hot_f
            c = c + 1.0
    
    return ps / c



def getPeak(y,Fs):
    n = len(y) # lungime semnal
    k = arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    frq = frq[range(int(n/2))] # one side frequency range

    Y = fft(y)/n # fft computing and normalization
    Y = abs(Y[range(int(n/2))])

    fr = 0
    mag = 0

    for i in range(0,len(Y)):
        if frq[i] >= 2500 and frq[i] <= 3000:
            if Y[i] > mag:
                fr = frq[i]
                mag = Y[i]
        
    #print(fr, mag)  
    """plot(frq,Y,'r') # plotting the spectrum
    xlabel('Freq (Hz)')
    ylabel('|Y(freq)|')
    show()
    """

    return fr

cold = 7
rate,data=read('7c_water.wav')
y=data[:,1]
cold_f = window(y)
print("Cold train freq: ",cold_f)

hot = 100
rate,data=read('hot_water.wav')                                                                             
y=data[:,1] 
hot_f = window(y)
print("Hot train freq: ",hot_f)

rate,data=read('test_47C.wav')
y=data[:,1]
x = window(y)
print("Test ",x)


m = (cold-hot)/(cold_f-hot_f)

#y − y1 = m(x − x1)
#y = m(x - x1) + y1
#print("Grad",m)
#y = (m*x - m*cold_f) + cold

y = -m*x + (-m*-hot_f) + cold

print(y)

