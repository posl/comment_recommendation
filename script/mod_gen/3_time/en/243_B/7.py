def main():
	N = int(input())
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))
	
	A_dict = {}
	B_dict = {}
	
	for i in range(N):
		A_dict[A[i]] = i
		B_dict[B[i]] = i
	
	#1.
	same = 0
	for i in range(N):
		if A[i] in B_dict and i == B_dict[A[i]]:
			same += 1
	print(same)
	
	#2.
	diff = 0
	for i in range(N):
		if A[i] in B_dict and i != B_dict[A[i]]:
			diff += 1
	print(diff)

if __name__ == '__main__':
    main()