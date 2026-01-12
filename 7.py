# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square
from scipy.signal import sawtooth
from scipy.io import wavfile

# 7.1

f = 5
L = 1
f_m = 1000
N = L * f_m
T = L / N
f_t = 1 / (2*T)
# Parameters

t = np.linspace(0, L, N, endpoint=False)
f_eix = np.linspace(-f_t, f_t, N, endpoint=False)
# Temporal and frequencial axis

g1 = square(2*np.pi*f*t)
g2 = sawtooth(2*np.pi*f*t)
# Square and sawtooth wave building

G1 = np.fft.fftshift(np.fft.fft(g1))
G1_abs = np.abs(G1)
G2 = np.fft.fftshift(np.fft.fft(g2))
G2_abs = np.abs(G2)
# Square and sawtooth wave transformation

def rect(f, l): 
    return np.where(np.abs(f) <= l/2, 1, 0)
# Rectangle function construction

G1_f = G1 * rect(f_eix, 2*f)
G2_f = G2 * rect(f_eix, 2*f)
# Applying the low-pass filter to the transformed waves

g1_f = np.real(np.fft.ifft(np.fft.ifftshift(G1_f)))
g2_f = np.real(np.fft.ifft(np.fft.ifftshift(G2_f)))
# Inverse transformation of the filtered transformed waves

plt.figure(figsize=(10, 10))
plt.suptitle("Ona cuadrada")

plt.subplot(221)
plt.plot(t, g1)
plt.title("g(t)")
plt.ylabel("g")
plt.xlabel("t(s)")
plt.grid(True)

plt.subplot(222)
plt.plot(f_eix, G1_abs)
plt.title("|G(f)|")
plt.ylabel("|G|")
plt.xlabel("f(Hz)")
plt.grid(True)

plt.subplot(223)
plt.plot(f_eix, np.abs(G1_f))
plt.title("|G(f)·rect(f/l)|")
plt.ylabel("|G·rect|")
plt.xlabel("f(Hz)")
plt.grid(True)

plt.subplot(224)
plt.plot(t, g1_f)
plt.title("g_f(t)")
plt.ylabel("g_f")
plt.xlabel("t(s)")
plt.grid(True)

plt.tight_layout()

plt.figure(figsize=(10, 10))
plt.suptitle("Ona dent de serra")

plt.subplot(221)
plt.plot(t, g2)
plt.title("g(t)")
plt.ylabel("g")
plt.xlabel("t(s)")
plt.grid(True)

plt.subplot(222)
plt.plot(f_eix, G2_abs)
plt.title("|G(f)|")
plt.ylabel("|G|")
plt.xlabel("f(Hz)")
plt.grid(True)

plt.subplot(223)
plt.plot(f_eix, np.abs(G2_f))
plt.title("|G(f)·rect(f/l)|")
plt.ylabel("|G·rect|")
plt.xlabel("f(Hz)")
plt.grid(True)

plt.subplot(224)
plt.plot(t, g2_f)
plt.title("g_f(t)")
plt.ylabel("g_f")
plt.xlabel("t(s)")
plt.grid(True)

plt.tight_layout()

# 7.2

f = 440
L = 3
f_m = 44100
N = L * f_m
# Parameters

t = np.linspace(0, L, N, endpoint=False)
# Time axis

g = np.sin(2 * np.pi * f * t)
# Sinusoidal wave of 440Hz

#wavfile.write('diapaso_440Hz.wav', f_m, g.astype(np.float32))
# Storage of the sinusoidal wave of f = 440Hz digitized at f_m = 44100Hz

#7.3 

f_m, g = wavfile.read('piano-la3.wav')
# Reading the file

L = 1
N = L * f_m
T = L / N
f_t = 1 / (2*T)
f_f = 440
# Parameters

t = np.linspace(0, L, N, endpoint=False)
f_eix = np.linspace(-f_t, f_t, N, endpoint=False)
# Creating time and frequency axis 

g = g[:N]
# Slizing the file

G = np.fft.fftshift(np.fft.fft(g))
G_abs = np.abs(G)
# Transforming the file

G_f = G * rect(f_eix, 2*f_f)
# Filtered transformed wave

g_f = np.real(np.fft.ifft(np.fft.ifftshift(G_f)))
# Inverse transformation of the filtered transformed wave

plt.figure(figsize=(10, 10))
plt.suptitle('Ona de piano')

plt.subplot(221)
plt.plot(t[:int(len(t) * 0.01)], g[:int(len(t) * 0.01)])
plt.title("g(t)")
plt.ylabel("g")
plt.xlabel("t(s)")
plt.grid(True)

plt.subplot(222)
plt.plot(f_eix[len(f_eix)//2:], G_abs[len(G_abs)//2:])
plt.title("G(f)")
plt.ylabel("G")
plt.yscale('log')
plt.xlabel("f(Hz)")
plt.grid(True)

plt.subplot(223)
plt.plot(f_eix[len(f_eix)//2:], G_f[len(G_f)//2:])
plt.title("|G(f)·rect(f/l)|")
plt.ylabel("|G·rect|")
plt.xlabel("f(Hz)")
plt.grid(True)

plt.subplot(224)
plt.plot(t[:int(len(t) * 0.01)], g_f[:int(len(t) * 0.01)])
plt.title("g_f(t)")
plt.ylabel("g_f")
plt.xlabel("t(s)")
plt.grid(True)

plt.tight_layout()

#g_f_norm = g_f / np.max(np.abs(g_f))
#wavfile.write('piano_440Hz.wav', f_m, g_f_norm.astype(np.float32))
# Normalizing the filtered wave and storing it






