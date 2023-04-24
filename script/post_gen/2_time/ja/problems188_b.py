Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i] * B[i]
    if ans == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

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
Suggestion 3

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        ans += a[i]*b[i]
    if ans == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

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
Suggestion 5

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    ans = 0
    for i in range(n):
        ans += a[i] * b[i]
    if ans == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ab = [a[i]*b[i] for i in range(n)]
    if sum(ab) == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = "Yes"
    for i in range(N):
        if A[i] * B[i] != 0:
            ans = "No"
            break
    print(ans)

=======
Suggestion 8

def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #内積
    inner_product = 0
    for i in range(N):
        inner_product += A[i] * B[i]
    #出力
    if inner_product == 0:
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
    inner_product = 0
    for i in range(N):
        inner_product += A[i]*B[i]
    
    #出力
    if inner_product == 0:
        print('Yes')
    else:
        print('No')
