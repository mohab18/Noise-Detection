import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft

duration = 8
N=14*1024
f=np.linspace(0,512,int(N/2))
t = np.linspace(0,14,12*1024)
fn2,fn1=np.random.randint(0,512,2)

n=np.sin(2*np.pi*fn1*t)+np.sin(2*np.pi*fn2*t)

G_key_freq = 196.0

D_key_freq = 293.66

E_key_freq = 329.63

C_key_freq = 261.63

B_key_freq = 246.93

A_key_freq = 220.0

def create_key(start_time, end_time, frequency):
    unit_step = np.where(t >= start_time, 1, 0)
    shifted_unit_step = np.where(t >= start_time+end_time, 1, 0)
    key = np.sin(2 * np.pi * t * frequency)
    return key*(unit_step - shifted_unit_step)
    
# G Key from 0 - 0.8
key1 = create_key(0, 0.8,G_key_freq)

# G Key from 0.9 - 1.7
key2 = create_key(0.9, 0.8, G_key_freq)

# D Key from 1.8 to 2.6
key3 = create_key(1.8, 0.8, D_key_freq)

# D Key from 2.7 to 3.5
key4 = create_key(2.7, 0.8, D_key_freq)

# E Key from 3.6 to 4.4
key5 = create_key(3.6, 0.8, E_key_freq)

# E Key from 4.5 to 5.3
key6 = create_key(4.5, 0.8, E_key_freq)

# D Key from 5.4 to 6.6
key7 = create_key(5.4, 1.1, D_key_freq)

# C Key from 7 to 7.8
key8 = create_key(7, 0.8, C_key_freq)

# C Key from 7.9 to 8.7
key9 = create_key(7.9, 0.8, C_key_freq)

# B Key from 8.8 to 9.6
key10 = create_key(8.8, 0.8, B_key_freq)

# B Key from 9.7 to 10.5
key11 = create_key(9.7, 0.8, B_key_freq)

# A Key from 10.6 to 11.4
key12 = create_key(10.6, 0.8, A_key_freq)

# A Key from 11.5 to 12.3
key13 = create_key(11.5, 0.8, A_key_freq)

# G Key from 12.4 to 13.2
key14 = create_key(12.4, 0.8, G_key_freq)



song = key1+key2+key3+key4+key5+key6+key7+key8+key9+key10+key11+key12+key13+key14
songwithnoise=song+n
x_fno=fft(song)
x_fno= 2/N * np.abs(x_fno[0:np.int(N/2)])
x_f=fft(songwithnoise)
m = round(max(x_fno))
x_f=2/N*np.abs(x_f[0:np.int(N/2)])
myNoise=[]
j=0;
for i in range(len(f)):
    if (round(x_f[i]) > m):
       
        myNoise+=[f[i]]
        
        

f1n=round(myNoise[0])
f2n=round(myNoise[1])

songwithoutnoise=songwithnoise-(np.sin(2*np.pi*fn1*t)+np.sin(2*np.pi*fn2*t))
songwithoutnoise_f=fft(songwithoutnoise)
songwithoutnoise_f = 2/N * np.abs(songwithoutnoise_f[0:np.int(N/2)])


plt.subplot(6,2,1)
plt.plot(t,song)
plt.subplot(6,2,2)
plt.plot(f,x_fno)
plt.subplot(6,2,3)
plt.plot(t,songwithnoise)
plt.subplot(6,2,4)
plt.plot(f,x_f)
plt.subplot(6,2,5)
plt.plot(t,songwithoutnoise)
plt.subplot(6,2,6)
plt.plot(f,songwithoutnoise_f)

sd.play(songwithoutnoise, 2*1024)


