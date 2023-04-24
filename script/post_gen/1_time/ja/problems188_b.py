Synthesizing 10/10 solutions

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
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        ans += a[i]*b[i]
    if ans == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if sum([a*b for a, b in zip(A, B)]) == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print("Yes" if sum([a[i]*b[i] for i in range(n)]) == 0 else "No")

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if sum([a*b for a,b in zip(A, B)]) == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = 0
    for i in range(N):
        a += A[i] * B[i]
    if a == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    #計算
    ans = 0
    for i in range(N):
        ans += A[i] * B[i]

    #出力
    if ans == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    #print(a)
    #print(b)
    sum = 0
    for i in range(n):
        sum += a[i] * b[i]
    #print(sum)
    if sum == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    N = int(input()) # Nを入力
    A = list(map(int, input().split())) # Aを入力
    B = list(map(int, input().split())) # Bを入力
    ans = 0
    for i in range(N):
        ans += A[i] * B[i]
    if ans == 0:
        print("Yes")
    else:
        print("No")
