Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if A[i] != A[j] and A[j] != A[k] and A[k] != A[i]:
                    if A[i] < A[j] < A[k] or A[k] < A[j] < A[i]:
                        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int,input().split()))
    count = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if a[i] == a[j] or a[j] == a[k] or a[k] == a[i]:
                    continue
                elif a[i] + a[j] > a[k] and a[i] + a[k] > a[j] and a[j] + a[k] > a[i]:
                    count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if A[i] != A[j] and A[j] != A[k] and A[k] != A[i]:
                    if A[i] < A[j] < A[k] or A[k] < A[j] < A[i]:
                        cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if a[i] != a[j] and a[j] != a[k] and a[k] != a[i]:
                    if a[i] < a[j] < a[k] or a[i] > a[j] > a[k]:
                        ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #A = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9]
    #N = len(A)
    A.sort()
    #print(A)
    #print(N)
    #print(A[0],A[1],A[2])
    #print(A[0],A[1],A[3])
    #print(A[0],A[2],A[3])
    #print(A[1],A[2],A[3])
    #print(A[1],A[2],A[4])
    #print(A[1],A[3],A[4])
    #print(A[2],A[3],A[4])
    #print(A[2],A[3],A[5])
    #print(A[2],A[4],A[5])
    #print(A[3],A[4],A[5])
    #print(A[3],A[4],A[6])
    #print(A[3],A[5],A[6])
    #print(A[4],A[5],A[6])
    #print(A[4],A[5],A[7])
    #print(A[4],A[6],A[7])
    #print(A[5],A[6],A[7])
    #print(A[5],A[6],A[8])
    #print(A[5],A[7],A[8])
    #print(A[6],A[7],A[8])
    #print(A[6],A[7],A[9])
    #print(A[6],A[8],A[9])
    #print(A[7],A[8],A[9])
    #print(A[7],A[8],A[10])
    #print(A[7],A[9],A[10])
    #print(A[8],A[9],A[10])
    #print(A[8],A[9],A[11])
    #print(A[8],A[10],A[11])
    #print(A[9],A[10],A[11])
    #print(A[

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if A[i] != A[j] and A[j] != A[k] and A[k] != A[i]:
                    ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 長さ N の数列 A=(A_1,A_2,...,A_N) が与えられます。
    # 以下の 2 条件をともに満たすような整数の組 (i,j,k) の個数を求めてください。
    # 1≦ i < j < k ≦ N
    # A_i,A_j,A_k は相異なる
    #
    # 制約
    # 3 ≦ N ≦ 2× 10^5
    # 1 ≦ A_i ≦ 2× 10^5
    # 入力に含まれる値は全て整数である

    # A = [3, 1, 4, 1]
    # A = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990]
    # A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]

    # A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
    # A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
    # A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
    # A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]

    # 1 <= i < j

=======
Suggestion 8

def main():
    import sys
    input = sys.stdin.readline
    from collections import Counter
    N = int(input())
    A = list(map(int,input().split()))
    C = Counter(A)
    ans = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            if A[i] != A[j]:
                ans += N - j - 1 - C[A[i]] - C[A[j]]
                C[A[i]] -= 1
    print(ans)

=======
Suggestion 9

def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    #リストAの各要素の出現回数をカウント
    count = [0] * (2 * 10**5 + 1)
    for i in range(N):
        count[A[i]] += 1
    #組み合わせの数を数える
    ans = 0
    for i in range(1, 2 * 10**5 + 1):
        if count[i] >= 2:
            ans += count[i] * (count[i] - 1) // 2
    #出力
    for i in range(N):
        if count[A[i]] >= 2:
            print(ans - count[A[i]] * (count[A[i]] - 1) // 2 + (count[A[i]] - 1) * (count[A[i]] - 2) // 2)
        else:
            print(ans)
