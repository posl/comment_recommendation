Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def solve(h, w, k, c):
    ans = 0
    for i in range(2**h):
        for j in range(2**w):
            cnt = 0
            for k1 in range(h):
                for l1 in range(w):
                    if (i >> k1) & 1 == 0 and (j >> l1) & 1 == 0 and c[k1][l1] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1
    return ans

=======
Suggestion 3

def main():
    H,W,K = map(int,input().split())
    c = [list(input()) for i in range(H)]
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if i>>k & 1:
                        continue
                    if j>>l & 1:
                        continue
                    if c[k][l] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    h,w,k = map(int,input().split())
    c = [list(input()) for i in range(h)]
    ans = 0
    for i in range(2 ** h):
        for j in range(2 ** w):
            cnt = 0
            for x in range(h):
                for y in range(w):
                    if (i >> x) & 1 == 0 and (j >> y) & 1 == 0 and c[x][y] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)

main()

=======
Suggestion 5

def get_input():
    h, w, k = map(int, input().split())
    c = []
    for i in range(h):
        c.append(list(input()))
    return h, w, k, c

=======
Suggestion 6

def main():
    H, W, K = map(int, input().split())
    c = [input() for _ in range(H)]
    ans = 0
    for i in range(2 ** H):
        for j in range(2 ** W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if i >> k & 1 and j >> l & 1 and c[k][l] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1

    print(ans)

=======
Suggestion 7

def main():
	h, w, k = map(int, input().split())
	grid = [list(input()) for _ in range(h)]
	ans = 0
	for i in range(2 ** h):
		for j in range(2 ** w):
			cnt = 0
			for x in range(h):
				for y in range(w):
					if (i >> x) & 1 == 0 and (j >> y) & 1 == 0 and grid[x][y] == '#':
						cnt += 1
			if cnt == k:
				ans += 1
	print(ans)
