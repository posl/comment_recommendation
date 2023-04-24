Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, D = map(int, input().split())
    L, R = [], []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)

    L.sort()
    R.sort()

    ans = 0
    for i in range(N):
        ans += max(0, L[i] - R[i - 1] - D)
        ans += max(0, R[i] - L[i + 1] - D)

    print(ans)

main()

=======
Suggestion 2

def main():
    N, D = map(int, input().split())
    walls = []
    for _ in range(N):
        L, R = map(int, input().split())
        walls.append((L, R))
    walls.sort()
    ans = 0
    i = 0
    while i < N:
        j = i
        while j < N and walls[j][0] <= walls[i][1] + D:
            j += 1
        ans += 1
        i = j
    print(ans)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    walls = []
    for i in range(N):
        L, R = map(int, input().split())
        walls.append((L, R))
    walls.sort()
    ans = 0
    i = 0
    while i < N:
        j = i
        while j < N and walls[j][0] <= walls[i][0] + D - 1:
            j += 1
        ans += 1
        i = j
    print(ans)

=======
Suggestion 4

def main():
    N, D = map(int, input().split())
    walls = []
    for i in range(N):
        L, R = map(int, input().split())
        walls.append([L, R])
    walls.sort()
    ans = 0
    idx = 0
    while idx < N:
        ans += 1
        for i in range(idx, N):
            if walls[i][0] <= walls[idx][0] + D - 1:
                idx += 1
            else:
                break
    print(ans)

=======
Suggestion 5

def main():
    n, d = map(int, input().split())
    l, r = [], []
    for _ in range(n):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)

    l.sort()
    r.sort()

    ans = 0
    for i in range(n):
        ans += l[i] + r[i] - d

    print(ans)

=======
Suggestion 6

def main():
    N, D = map(int, input().split())
    walls = [tuple(map(int, input().split())) for _ in range(N)]
    walls.sort(key=lambda x: x[1])
    ans = 0
    i = 0
    while i < N:
        ans += 1
        j = i
        while j < N and walls[j][0] + D - 1 >= walls[i][1]:
            j += 1
        i = j
    print(ans)

=======
Suggestion 7

def main():
    N,D = map(int,input().split())
    walls = []
    for i in range(N):
        L,R = map(int,input().split())
        walls.append([L,R])
    walls.sort()
    ans = 0
    for i in range(N):
        if walls[i][0] >= 0:
            ans += 1
            walls[i][0] = -1
            for j in range(i+1,N):
                if walls[j][0] >= 0:
                    if walls[j][0] <= walls[i][1]+D:
                        walls[j][0] = -1
                    else:
                        break
    print(ans)

=======
Suggestion 8

def  main():
    N, D = map(int, input().split())
    walls = []
    for  _  in  range(N):
        L, R = map(int, input().split())
        walls.append((L, R))
    walls.sort()

    ans = 0
    r = 0
    for  l, r  in  walls:
        if  r - l + 1  <=  D:
            ans += 1
            continue
        if  r  <  l + D - 1:
            continue
        if  r  <  l + D:
            ans += 1
            continue
        ans += 2

    print(ans)

=======
Suggestion 9

def main():
    import sys
    readline = sys.stdin.readline

    N, D = map(int, readline().split())
    LR = [list(map(int, readline().split())) for _ in range(N)]

    LR.sort(key=lambda x: x[0])
    ans = 0
    r = -1
    for l, r in LR:
        if r <= r:
            continue
        ans += -(-((r - l) // D))
        r = l + D * ans
    print(ans)

=======
Suggestion 10

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
