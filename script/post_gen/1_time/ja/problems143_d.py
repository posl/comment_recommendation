Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] + L[j] > L[k]:
                    ans += 1
    print(ans)

=======
Suggestion 2

def solve():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                    if L[i] + L[j] > L[k]:
                        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    cnt = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] < L[j] + L[k]:
                    cnt += 1
                else:
                    break
    print(cnt)

=======
Suggestion 4

def solve():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] + L[j] > L[k] and L[j] + L[k] > L[i] and L[k] + L[i] > L[j]:
                    ans += 1
    print(ans)

=======
Suggestion 5

def solve():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i]+L[j] > L[k] and L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                    ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N-2):
        a = L[i]
        for j in range(i+1, N-1):
            b = L[j]
            for k in range(j+1, N):
                c = L[k]
                if a < b + c and b < c + a and c < a + b:
                    ans += 1
    print(ans)

=======
Suggestion 7

def main():
    # N = int(input())
    # L = list(map(int, input().split()))
    N = 7
    L = [218, 786, 704, 233, 645, 728, 389]
    # N = 4
    # L = [3, 4, 2, 1]
    # N = 3
    # L = [1, 1000, 1]

    ans = 0
    L.sort()
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if L[i] + L[j] > L[k]:
                    ans += 1
                else:
                    break
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()

    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k]:
                    ans += 1
                else:
                    break
    print(ans)

=======
Suggestion 9

def check(a,b,c):
	if a < b + c and b < c + a and c < a + b:
		return True
	else:
		return False

N = int(input())
L = list(map(int,input().split()))
L.sort()
ans = 0
for i in range(N):
	for j in range(i+1,N):
		for k in range(j+1,N):
			if check(L[i],L[j],L[k]):
				ans += 1
print(ans)

=======
Suggestion 10

def get_input():
    n = int(input())
    l = list(map(int, input().split()))
    return n, l
