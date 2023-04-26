Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        sum += A[i] * B[i]
    if sum == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if sum([a[i] * b[i] for i in range(n)]) == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if sum([a[i] * b[i] for i in range(n)]) == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if sum([A[i]*B[i] for i in range(N)]) == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = 0
    for i in range(n):
        c += a[i] * b[i]
    if c == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    if sum([a[i]*b[i] for i in range(n)]) == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print('Yes' if sum([A[i]*B[i] for i in range(N)]) == 0 else 'No')

=======
Suggestion 8

def main():
    # 1行目
    n = int(input())
    # 2行目
    a = list(map(int, input().split()))
    # 3行目
    b = list(map(int, input().split()))
    
    # AとBの内積
    ab = 0
    for i in range(n):
        ab += a[i] * b[i]
    
    # 内積が0かどうか判定
    if ab == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #内積
    ans = 0
    for i in range(N):
        ans += A[i]*B[i]
    #出力
    if ans == 0:
        print("Yes")
    else:
        print("No")
