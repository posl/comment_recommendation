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
    T = list(map(int, input().split()))
    T.sort()
    ans = 0
    for i in range(N-1):
        ans += T[i]
    ans += T[-1]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    T = list(map(int, input().split()))
    print(sum(T) - max(T) // 2)

=======
Suggestion 4

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    print(sum(T) - T[-1] + T[-1] // 2)

=======
Suggestion 5

def main():
    N = int(input())
    T = [int(i) for i in input().split()]
    T.sort()
    ans = 0
    for i in range(N-1):
        ans += T[i]
    ans += T[N-1]
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    print(T[-1] + sum(T[:-1]))

=======
Suggestion 7

def main():
    N = int(input())
    T = list(map(int,input().split()))
    T.sort(reverse=True)
    if N == 1:
        print(T[0])
    else:
        print(T[0]+T[1])

=======
Suggestion 8

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort(reverse=True)
    ans = T[0]
    for i in range(1,N):
        ans = ans + T[i]
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    T.reverse()
    print(sum(T) - T[0] + T[0] // 2)
