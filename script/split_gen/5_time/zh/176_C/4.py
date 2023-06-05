def main():
	n = int(input())
	a = [int(x) for x in input().split()]
	# print(n)
	# print(a)
	ans = 0
	# for i in range(n):
	# 	ans += max(0, a[i] - a[i-1])
	# print(ans)
	for i in range(n-1):
		ans += max(0, a[i] - a[i+1])
	ans += max(0, a[n-1])
	print(ans)
