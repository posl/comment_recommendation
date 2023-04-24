Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        ans += (B[i] - A[i] + 1) * (A[i] + B[i]) / 2
    print(int(ans))

=======
Suggestion 2

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    ans = 0
    for i in range(N):
        ans += (B[i] - A[i] + 1) * (A[i] + B[i]) / 2

    ans = int(ans % (10**9 + 7))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        ans += (B[i] - A[i] + 1) * (A[i] + B[i]) // 2
    print(ans % (10**9 + 7))

=======
Suggestion 4

def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    
    sum = 0
    for i in range(n):
        sum += (b[i] - a[i] + 1) * (a[i] + b[i]) // 2
    
    print(sum % 998244353)

=======
Suggestion 5

def main():
    N = int(input())
    cnt = 0
    for i in range(N):
        A, B = map(int, input().split())
        cnt += (B - A + 1) * (A + B) // 2
    print(cnt % (10 ** 9 + 7))

=======
Suggestion 6

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for i in range(N)]
    
    ans = 0
    for i in range(N):
        ans += (AB[i][1] - AB[i][0] + 1) * (AB[i][0] + AB[i][1]) // 2
    
    print(ans % 1000000007)

=======
Suggestion 7

def main():
    #入力
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    #処理
    ans = 0
    for i in range(N):
        ans += (AB[i][1] - AB[i][0] + 1) * (AB[i][0] + AB[i][1]) // 2
    #出力
    print(ans)

=======
Suggestion 8

def main():
    #入力
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    #初期化
    ans = 0
    #処理
    for i in range(N):
        ans += (AB[i][1] - AB[i][0] + 1) * (AB[i][0] + AB[i][1]) // 2
    #出力
    print(ans % (10 ** 9 + 7))

=======
Suggestion 9

def main():
    N = int(input()) # N 回の操作を行う
    A = [0]*N # A_i 以上の整数を書く
    B = [0]*N # B_i 以下の整数を書く
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    ans = 0
    for i in range(N):
        ans += (B[i] - A[i] + 1) * (A[i] + B[i]) // 2

    print(ans % (10**9 + 7))
