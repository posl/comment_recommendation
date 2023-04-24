Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(N):
        if a[i] <= ans + 1:
            ans += a[i]
        else:
            break
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if A[i] <= ans + 1:
            ans += A[i]
        else:
            break
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] == ans + 1:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if ans + 1 == a[i]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if ans + 1 < A[i]:
            break
        ans += A[i]
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if a[i] > a[i-1] + 1:
            break
        ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    A.sort()
    ans = 0
    for i in range(N):
        if A[i] >= ans + 1:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    # 1. 入力
    n = int(input())
    a = list(map(int, input().split()))
    # 2. 計算
    # 2.1. a をソート
    a.sort()
    # 2.2. a の最大値を求める
    max_a = a[-1]
    # 2.3. a の最大値の約数を求める
    divisor = []
    for i in range(1, int(max_a**0.5)+1):
        if max_a % i == 0:
            divisor.append(i)
            if max_a // i != i:
                divisor.append(max_a // i)
    # 2.4. a の最大値の約数で割り切れる数を求める
    divisor.sort()
    for d in divisor:
        if all([ai % d == 0 for ai in a]):
            ans = d
    # 3. 出力
    print(ans)
