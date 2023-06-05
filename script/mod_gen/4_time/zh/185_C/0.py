def cutbar(m,n,current):
	if current >= n:
		return 0
	elif current < m:
		return 1 + cutbar(m,n,current*2)
	else:
		return 1 + cutbar(m,n,current + m)
print(cu

if __name__ == '__main__':
    cutbar()