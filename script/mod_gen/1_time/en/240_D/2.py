def main():
	n = int(input())
	a = list(map(int, input().split()))
	b = [0] * (2 * 10 ** 5 + 1)
	for i in range(n):
		b[a[i]] += 1
	s = 0
	for i in range(2 * 10 ** 5, 1, -1):
		b[i - 1] += b[i] // 2
		s += b[i] % 2
		b[i] = 0
		print(s)
main()

if __name__ == '__main__':
    main()