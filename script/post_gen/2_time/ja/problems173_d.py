Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    for i in range(1, n):
        ans += a[i // 2]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (N - i - 1)
        ans += A[i] * i
    print(ans)

main()

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N - 1):
        ans += A[i] * (N - i - 1)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (N - i - 1)
        ans -= A[i] * i
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (2 * i - n + 1)
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(1, n):
        ans += a[i] * i
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort(reverse=True)
    ans = 0
    for i in range(1, N):
        ans += A[i//2]
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N):
        ans += A[i] * (2**(N-i-1) - 2**i)
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    #Aを降順にソート
    A.sort(reverse=True)
    
    #Aの最大値は、Aの中央値の2倍以上になることはない
    #Aの中央値をxとすると、xの左側の数の合計は、xの右側の数の合計よりも大きくなる
    #xの左側の数の合計は、xの右側の数の合計よりも小さくなる
    #xの左側の数の合計は、xの右側の数の合計と等しい
    #xの左側の数の合計は、xの右側の数の合計よりも大きくなり、xの左側の数の合計は、xの右側の数の合計と等しい
    #xの左側の数の合計は、xの右側の数の合計よりも小さくなり、xの左側の数の合計は、xの右側の数の合計と等しい
    #xの左側の数の合計は、xの右側の数の合計よりも大きくなり、xの左側の数の合計は、xの右側の数の合計よりも小さくなる
    #xの左側の数の合計は、xの右側の数の合計よりも小さくなり、xの左側の数の合計は、xの右側の数の合計よりも大きくなる
    #xの左側の数の合計は、xの右側の数の合計よりも大きくなり、xの左側の数の合計は、xの右側の数の合計よりも小さくなり、xの左側の数の合計

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()  # 逆順にしたいので降順にソート
    A.reverse()

    ans = 0
    for i in range(N):
        if i % 2 == 0:
            ans += A[i]
        else:
            ans -= A[i]

    print(ans)
