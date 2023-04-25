Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] != T[i][j]:
                print('No')
                return
    print('Yes')

=======
Suggestion 2

def readinput():
    h,w=readArray(int)
    s=[]
    for _ in range(h):
        s.append(input())
    t=[]
    for _ in range(h):
        t.append(input())
    return h,w,s,t

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = []
    T = []
    for i in range(H):
        S.append(input())
    for i in range(H):
        T.append(input())
    S = sorted(S)
    T = sorted(T)
    for i in range(H):
        if S[i] != T[i]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    T = [input() for i in range(H)]
    for i in range(H):
        if S[i].count('#') != T[i].count('#'):
            print('No')
            exit()
    print('Yes')
main()

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    T = [input() for i in range(H)]
    if sorted(S) == sorted(T):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def solve():
    h, w = map(int, input().split())
    s = [input() for i in range(h)]
    t = [input() for i in range(h)]
    print("Yes" if sorted(s) == sorted(t) else "No")

=======
Suggestion 7

def main():
    H, W = list(map(int, input().split()))
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    for i in range(H):
        if sorted(S[i]) != sorted(T[i]):
            print("No")
            return
    for j in range(W):
        if sorted([S[i][j] for i in range(H)]) != sorted([T[i][j] for i in range(H)]):
            print("No")
            return
    print("Yes")

main()

=======
Suggestion 8

def solve():
    H,W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    S = [sorted(S[i]) for i in range(H)]
    T = [sorted(T[i]) for i in range(H)]
    S.sort()
    T.sort()
    for i in range(H):
        if S[i] != T[i]:
            return "No"
    return "Yes"

=======
Suggestion 9

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

=======
Suggestion 10

def check_pattern(S, T):
    S = sorted(S)
    T = sorted(T)
    if S == T:
        return True
    else:
        return False
