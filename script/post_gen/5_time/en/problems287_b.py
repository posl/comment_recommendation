Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    cnt = 0
    for s in S:
        for t in T:
            if s[-3:] == t:
                cnt += 1
                break
    print(cnt)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    count = 0
    for i in range(n):
        for j in range(m):
            if s[i][3:] == t[j]:
                count += 1
    print(count)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][3:6] == t[j]:
                ans += 1
                break
    print(ans)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]

    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][3:6] == t[j]:
                ans += 1
                break

    print(ans)

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    count = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                count += 1
    print(count)

=======
Suggestion 6

def problem287_b():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]

    count = 0
    for si in s:
        for ti in t:
            if si[-3:] == ti:
                count += 1
                break

    print(count)

=======
Suggestion 7

def get_input():
    n,m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    return n,m,s,t

=======
Suggestion 8

def problem():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    print(len(set(s) & set(t)))

problem()

=======
Suggestion 9

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

=======
Suggestion 10

def check_if_substring(s, t):
    if t in s:
        return True
    else:
        return False
