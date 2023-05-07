def main():
	N = int(input())
	A = list(map(int, input().split()))
	B = sorted(A)
	C = [0]*N
	for i in range(N):
		C[i] = B[i]
		if i > 0 and B[i] == B[i-1]:
			C[i] = 0
			C[i-1] = 0
	C = [c for c in C if c > 0]
	if len(C) == 0:
		print(0)
		return
	D = [0]*len(C)
	for i in range(len(C)):
		D[i] = A.index(C[i])
		A[D[i]] = -1
	E = sorted(D)
	if E == D:
		print(1)
	else:
		print(2)
