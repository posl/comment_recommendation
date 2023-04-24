Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > 10:
            ans += A[i] - 10

    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        if A[i] > 10:
            sum += A[i] - 10
    print(sum)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if A[i] > 10:
            cnt += A[i] - 10
    print(cnt)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > 10:
            ans += (A[i] - 10)
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum([a-10 for a in A if a>10]))

main()
