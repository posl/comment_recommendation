def main():
	N, D = [int(x) for x in input().split()]
	LR = [[int(x) for x in input().split()] for _ in range(N)]
	LR.sort(key=lambda x: x[1])
	ans = 0
	while LR:
		ans += 1
		x = LR[0][1] - D + 1
		for i in range(len(LR)):
			if LR[i][0] >= x:
				LR = LR[i:]
				break
			if i == len(LR) - 1:
				LR = []
	print(ans)

if __name__ == '__main__':
    main()