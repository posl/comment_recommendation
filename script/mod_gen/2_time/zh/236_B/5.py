def main():
	n = int(input())
	ai = list(map(int, input().split()))
	ai.sort()
	for i in range(0, len(ai), 2):
		if ai[i] != ai[i+1]:
			print(ai[i])
			break

if __name__ == '__main__':
    main()