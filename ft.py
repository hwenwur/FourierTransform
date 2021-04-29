import cmath


j = complex(0, 1)
conj = complex.conjugate
pi = cmath.pi
exp = cmath.exp


def DFT(xn):
	N = len(xn)
	W = exp(-j * 2 * pi / N)
	y = lambda n: sum([xn[i] * pow(W, i * n) for i in range(N)])
	yn = [y(i) for i in range(N)]
	return yn


def FFT(xn, N=-1):
	if N == -1:
		N = len(xn)

	if N == 1:
		return xn

	while N & (N - 1) != 0:
		xn.append(0)
		N += 1

	even_seq = [xn[i] for i in range(N) if i & 1 == 0]
	odd_seq = [xn[i] for i in range(N) if i & 1 != 0]

	fft_even = FFT(even_seq)
	fft_odd = FFT(odd_seq)

	W = exp(-j * 2 * pi / N)

	yn1 = [fft_even[i] + pow(W, i) * fft_odd[i] for i in range(N // 2)]
	yn2 = [fft_even[i] - pow(W, i) * fft_odd[i] for i in range(N // 2)]
	return [*yn1, *yn2][0:N]

