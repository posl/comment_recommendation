def permutation(n):
	if n == 0:
		yield []
	else:
		for i in range(n):
			for p in permutation(n-1):
				yield p[:i] + [n-1] + p[i:]

if __name__ == '__main__':
    permutation()