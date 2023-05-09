def main():
	n = int(input())
	ab = []
	for i in range(n):
		a, b = map(int, input().split())
		ab.append((a, b))
	ab.sort(key=lambda x: x[1])
	t = 0
	for a, b in ab:
		t += a
		if t > b:
			print('No')
			return
	print('Yes')
