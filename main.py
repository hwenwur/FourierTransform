import time
import random

from numpy.fft import fft as npfft
from ft import DFT, FFT


xn = [random.random() * 100 for i in range(2048)]

t0 = time.perf_counter() * 1000
r1 = DFT(xn)

t1 = time.perf_counter() * 1000
r2 = FFT(xn)

t2 = time.perf_counter() * 1000
r3 = npfft(xn)

t3 = time.perf_counter() * 1000

# 检验结果
assert len(r1) == len(r3), "DFT sequence length calculate error."
assert len(r2) == len(r3), "FFT sequence length calculate error."

for i in range(len(r3)):
	error1 = abs(r1[i] - r3[i])
	error2 = abs(r2[i] - r3[i])
	if error1 > 1e-3:
		print("DFT calculate error")
	if error2 > 1e-3:
		print("FFT calculate error")


print("--- cost time ---")
print("DFT: %.2fms" % (t1 - t0))
print("FFT: %.2fms" % (t2 - t1))
print("numpy fft: %.2fms" % (t3 - t2))

