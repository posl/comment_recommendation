def main():
	n, m = map(int, input().split())
	conditions = []
	for _ in range(m):
		a, b = map(int, input().split())
		conditions.append((a, b))
	k = int(input())
	people = []
	for _ in range(k):
		c, d = map(int, input().split())
		people.append((c, d))
	max_count = 0
	for i in range(2**k):
		balls = [0] * (n + 1)
		count = 0
		for j in range(k):
			if i >> j & 1:
				balls[people[j][0]] += 1
			else:
				balls[people[j][1]] += 1
		for condition in conditions:
			if balls[condition[0]] >= 1 and balls[condition[1]] >= 1:
				count += 1
		max_count = max(max_count, count)
	print(max_count)

if __name__ == '__main__':
    main()