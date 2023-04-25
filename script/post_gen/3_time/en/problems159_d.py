Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = [0] * (n + 1)
    for i in range(n):
        count[a[i]] += 1
    total = 0
    for i in range(n + 1):
        total += count[i] * (count[i] - 1) // 2
    for i in range(n):
        print(total - (count[a[i]] - 1))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*(N+1)
    for i in range(N):
        B[A[i]] += 1
    for i in range(N):
        print(N-1-B[A[i]])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = [0] * (N+1)
    for i in range(N):
        count[A[i]] += 1
    for i in range(N):
        print(N-1-count[A[i]])

=======
Suggestion 4

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [0] * (n + 1)
    for i in a:
        b[i] += 1
    ans = [0] * n
    for i in range(1, n+1):
        ans[i-1] = sum([b[j] for j in range(1, n+1) if j != i]) - b[i] + b[i] * (b[i] - 1) // 2
    print('

'.join(map(str, ans)))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for a in A:
        B[a-1] += 1
    for i in range(N):
        if B[i] == 0:
            print(0)
        else:
            print((B[i]-1)*B[i]//2)

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    count = [0] * (N + 1)
    for i in range(N):
        count[A[i]] += 1
    total = sum([count[i] * (count[i] - 1) // 2 for i in range(1, N + 1)])
    for i in range(N):
        print(total - (count[A[i]] - 1))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N+1)
    for i in A:
        B[i] += 1
    for i in range(1, N+1):
        if B[i] > 1:
            print((B[i] * (B[i]-1))//2)
        else:
            print(0)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    B = [0] * (N + 1)
    for i in range(N):
        B[A[i]] += 1
    #print(B)
    #print(sum(B))
    C = [0] * (N + 1)
    for i in range(N + 1):
        C[i] = B[i] * (B[i] - 1) // 2
    #print(C)
    D = sum(C)
    #print(D)
    for i in range(N):
        print(D - C[A[i]] + (B[A[i]] - 1) * (B[A[i]] - 2) // 2)

=======
Suggestion 9

def main():
    #input
    N = int(input())
    A = list(map(int, input().split()))
    #count
    B = [0]*(N+1)
    for i in A:
        B[i] += 1
    #output
    for i in range(N):
        print(B[A[i]]-1)

=======
Suggestion 10

def main():
    import sys
    from collections import Counter
    #入力
    readline = sys.stdin.readline
    N = int(readline())
    A = list(map(int, readline().split()))
    #処理
    #Aの要素の個数を数える
    counter = Counter(A)
    #Aの要素の個数をリストにする
    B = list(counter.values())
    #Aの要素の個数の合計を求める
    total = sum(B)
    #Aの要素の個数から2個選ぶ組み合わせの個数を求める
    C = [b*(total-b) for b in B]
    #出力
    for i in range(N):
        print(C[A[i]-1])
