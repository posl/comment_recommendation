def main():
	n = int(input())
	a = list(map(int, input().split()))
	
	max = 0
	x = 0
	for i in range(n):
		x += a[i]
		if x > max:
			max = x
	print(max)
