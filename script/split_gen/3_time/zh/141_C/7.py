def main():
	n,k,q = map(int,input().split())
	scores = [k for i in range(n)]
	for i in range(q):
		a = int(input())
		scores[a-1] -= 1
	for i in range(n):
		if scores[i] <= 0:
			print('No')
		else:
			print('Yes')
