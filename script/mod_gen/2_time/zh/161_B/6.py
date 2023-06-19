def main():
	n,m = map(int,input().split())
	A = list(map(int,input().split()))
	A.sort(reverse=True)
	total = sum(A)
	if A[m-1] >= total/(4*m):
		print("是")
	else:
		print("否")

if __name__ == '__main__':
    main()