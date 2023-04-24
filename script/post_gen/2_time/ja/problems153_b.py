Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    if H <= sum(A):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    print("Yes" if H <= sum(A) else "No")

=======
Suggestion 3

def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    print("Yes" if h <= sum(a) else "No")

=======
Suggestion 4

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[-1] >= H:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 6

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if H > A[-1]:
        print('No')
    else:
        print('Yes')

=======
Suggestion 7

def main():
    # 入力
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 処理
    if H <= sum(A):
        ans = "Yes"
    else:
        ans = "No"
    # 出力
    print(ans)

=======
Suggestion 8

def gcd(a,b):
    if a < b:
        a,b = b,a
    while b > 0:
        a,b = b,a%b
    return a

=======
Suggestion 9

def main():
    H,N = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    if H<=A[-1]:
        print("Yes")
    else:
        print("No")
