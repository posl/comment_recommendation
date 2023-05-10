def main():
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	s = [0] * (n + 1)
	for i in range(n):
		s[i + 1] = s[i] + a[i]
	#print(s)
	ans = 0
	r = 0
	for l in range(n):
		while r < n + 1 and s[r] - s[l] < k:
			r += 1
		if s[r] - s[l] == k:
			ans += 1
	print(ans)

if __name__ == '__main__':
    main()