Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    C = [0] * N
    for i in range(N):
        C[A[i]-1] += 1
    S = sum(C)
    for i in range(N):
        if C[A[i]-1] == 1:
            print(0)
        else:
            print(S - C[A[i]-1])

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    c = [0] * (N + 1)
    for a in A:
        c[a] += 1
    ans = 0
    for a in c:
        ans += a * (a - 1) // 2
    for a in A:
        print(ans - c[a] + 1)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    balls = [0] * N
    for a in A:
        balls[a - 1] += 1
    #print(balls)
    for b in balls:
        if b > 1:
            print(b * (b - 1) // 2)
        else:
            print(0)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # ボールの数をカウント
    cnt = [0] * N
    for i in range(N):
        cnt[A[i] - 1] += 1

    # 答えを計算
    ans = [0] * N
    for i in range(N):
        ans[i] = N * (N - 1) // 2 - (cnt[A[i] - 1] - 1)

    # 答えを出力
    for i in range(N):
        print(ans[i])

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #A = [1, 1, 2, 1, 2]
    #N = len(A)
    #print(N, A)
    #A = [3, 3, 3, 3, 3]
    #N = len(A)
    #print(N, A)
    #A = [1, 2, 1, 4, 2, 1, 4, 1]
    #N = len(A)
    #print(N, A)
    #A = [1, 2, 3, 4]
    #N = len(A)
    #print(N, A)
    #A = [3, 1, 2, 1, 2, 1, 2, 1]
    #N = len(A)
    #print(N, A)
    #A = [1, 1, 1, 1, 1, 1, 1, 1]
    #N = len(A)
    #print(N, A)
    #A = [1, 2, 3, 4, 5, 6, 7, 8]
    #N = len(A)
    #print(N, A)
    
    #A = [1, 2, 3, 4, 5, 6, 7, 8]
    #N = len(A)
    #print(N, A)
    
    #A = [1, 2, 3, 4, 5, 6, 7, 8]
    #N = len(A)
    #print(N, A)
    
    #A = [1, 2, 3, 4, 5, 6, 7, 8]
    #N = len(A)
    #print(N, A)
    
    #A = [1, 2, 3, 4, 5, 6, 7, 8]
    #N = len(A)
    #print(N, A)
    
    #A = [1, 2, 3, 4, 5, 6, 7, 8]
    #N = len(A)
    #print(N, A)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    A.append(0)
    count = 1
    ans = [0]*N
    for i in range(1,N+1):
        if A[i] == A[i-1]:
            count += 1
        else:
            ans[count-1] += 1
            count = 1
    for i in range(N):
        ans[i] = ans[i]*(ans[i]-1)//2
    for i in range(N-1):
        ans[i+1] += ans[i]
    for i in range(N):
        print(ans[N-i-1])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A

    # A[i]の出現回数を数える
    cnt = [0] * (N+1)
    for a in A:
        cnt[a] += 1

    # A[i]の出現回数の2乗の総和を求める
    sum = 0
    for i in range(N+1):
        sum += cnt[i] * cnt[i]

    # k=1,2,...,N のときの答えを出力
    for k in range(1, N+1):
        print((cnt[A[k]]-1) * (cnt[A[k]]-1) - (sum - cnt[A[k]] * cnt[A[k]]))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    # 1. Aの各要素の出現回数をカウント
    cnt = [0] * N
    for i in range(N):
        cnt[A[i]-1] += 1
    
    # 2. Aの各要素の出現回数を累積和
    for i in range(1,N):
        cnt[i] += cnt[i-1]
    
    # 3. Aの各要素の出現回数を使って、Aの各要素の出現回数の組み合わせを計算
    for i in range(N):
        res = (cnt[N-1] - cnt[A[i]-1]) * (cnt[A[i]-1] - 1) // 2
        print(res)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)

    #Aの中身をカウントする
    Acount = [0] * (N+1)
    for i in range(N):
        Acount[A[i]] += 1
    #print(Acount)

    #Acountの中身をカウントする
    Acountcount = [0] * (N+1)
    for i in range(N+1):
        Acountcount[Acount[i]] += 1
    #print(Acountcount)

    #Acountcountの中身をカウントする
    Acountcountcount = [0] * (N+1)
    for i in range(N+1):
        Acountcountcount[Acountcount[i]] += 1
    #print(Acountcountcount)

    #Acountcountcountの中身をカウントする
    Acountcountcountcount = [0] * (N+1)
    for i in range(N+1):
        Acountcountcountcount[Acountcountcount[i]] += 1
    #print(Acountcountcountcount)

    #Acountcountcountcountの中身をカウントする
    Acountcountcountcountcount = [0] * (N+1)
    for i in range(N+1):
        Acountcountcountcountcount[Acountcountcountcount[i]] += 1
    #print(Acountcountcountcountcount)

    #Acountcountcountcountcountの中身をカウントする
    Acountcountcountcountcountcount = [0] * (N+1)
    for i in range(N+1):
        Acountcountcountcountcountcount[Acountcountcountcountcount[i]] += 1
    #print(Acountcountcountcountcountcount)

    #Acountcountcountcountcountcountの中身をカウントする
    Acountcountcountcountcountcountcount = [0] * (N+1)
    for i in range(N+1):
        Acountcountcountcountcountcountcount[Acountcountcountcountcountcount[i]] += 1
    #print(Acountcountcountcountcountcountcount)

    #Acountcountcountcountcountcountcountの中身をカウントする

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = [0]*n
    # aの中の数字の個数をカウント
    cnt = [0]*n
    for i in range(n):
        cnt[a[i]-1] += 1
    # 重複組み合わせの計算
    for i in range(n):
        ans[i] = cnt[a[i]-1]*(cnt[a[i]-1]-1)//2
    # 重複組み合わせを引く
    for i in range(n):
        print(n*(n-1)//2-ans[i])
