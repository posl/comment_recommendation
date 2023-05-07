def pascal(n):
	if n == 0:
		return [1]
	else:
		return [1] + [pascal(n-1)[i-1] + pascal(n-1)[i] for i in range(1,n)] + [1]
