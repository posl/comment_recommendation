def main():
	h, w = map(int, input().split())
	s = [input() for _ in range(h)]
	t = [input() for _ in range(h)]
	
	s_count = [0] * w
	t_count = [0] * w
	
	for i in range(h):
		for j in range(w):
			if s[i][j] == '#':
				s_count[j] += 1
			if t[i][j] == '#':
				t_count[j] += 1
	
	for i in range(w):
		if s_count[i] != t_count[i]:
			print('No')
			return
	print('Yes')

if __name__ == '__main__':
    main()