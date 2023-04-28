Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    T = list(map(int, input().split()))
    print(sum(T) - max(T) + max(T) // 2)

=======
Suggestion 2

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    ans = 0
    for i in range(N):
        ans += T[i] * (N - i)
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
    ans = T[0]
    for i in range(1, N):
        ans += T[i]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    print(sum(T) - T[-1] + T[-1] // 2)

main()

=======
Suggestion 6

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    if n == 1:
        print(t[0])
    else:
        print(t[0] + sum(t[1:]) - t[0])
