Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        while a % 2 == 0:
            a //= 2
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] = A[i] / 2
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] /= 2
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        while a[i] % 2 == 0:
            ans += 1
            a[i] //= 2
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] /= 2
            cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
            else:
                print(cnt)
                return
        cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0

    while True:
        for i in range(n):
            if a[i] % 2 == 1:
                print(cnt)
                return
            else:
                a[i] /= 2
        cnt += 1

=======
Suggestion 8

def main():
    # 入力
    N = int(input())
    a = [int(x) for x in input().split()]

    # 処理
    count = 0
    while True:
        if all([x % 2 == 0 for x in a]):
            a = [x // 2 for x in a]
            count += 1
        else:
            break

    # 出力
    print(count)
