def main():
	W, H, x, y = map(int, input().split())
	area = W * H / 2
	if 2 * x == W and 2 * y == H:
		print(area, 1)
	else:
		print(area, 0)
