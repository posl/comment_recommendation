def main():
	n, m = map(int, input().split())
	s = [input() for i in range(n)]
	t = [input() for i in range(m)]
	
	s = set(s)
	t = set(t)
	
	# print(s)
	# print(t)
	
	ans = len(s & t)
	
	print(ans)

if __name__ == '__main__':
    main()