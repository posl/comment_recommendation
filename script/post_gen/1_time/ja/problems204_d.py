Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    ans = T[0]
    for i in range(1, N):
        ans += T[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    T = list(map(int,input().split()))
    T.sort()
    ans = 0
    for i in range(N):
        ans += T[i] * (N-i)
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    print(sum(T) - T[-1] + T[-1] // 2)

=======
Suggestion 4

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort(reverse=True)
    ans = t[0]
    for i in range(n-1):
        ans += t[i+1]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort(reverse=True)
    if N == 1:
        print(T[0])
    else:
        print(T[0]+sum(T[1:N-1])+int(T[N-1]/2))

=======
Suggestion 6

def main():
    N = int(input())
    T = list(map(int,input().split()))
    T.sort()
    if N == 1:
        print(T[0])
    else:
        oven1 = T[0]
        oven2 = T[1]
        for i in range(2,N):
            if oven1 < oven2:
                oven1 += T[i]
            else:
                oven2 += T[i]
        print(max(oven1,oven2))

=======
Suggestion 7

def main():
    N = int(input())
    T = list(map(int, input().split()))
    ans = 0
    T.sort()
    ans = T[-1]
    for i in range(N-1):
        ans += T[i]
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    print(T[N-1] + sum(T[:N-1]))
