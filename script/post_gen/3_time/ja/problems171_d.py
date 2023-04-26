Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = [0] * Q
    C = [0] * Q
    for i in range(Q):
        B[i], C[i] = map(int, input().split())

    # Aの要素の値がB[i]であるものの個数をカウント
    cnt = [0] * (10**5 + 1)
    for i in range(N):
        cnt[A[i]] += 1

    # 答えを求める
    ans = sum(A)
    for i in range(Q):
        ans += cnt[B[i]] * (C[i] - B[i])
        cnt[C[i]] += cnt[B[i]]
        cnt[B[i]] = 0
        print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = [0] * Q
    C = [0] * Q
    for i in range(Q):
        B[i], C[i] = map(int, input().split())
    S = [0] * Q
    S[0] = sum(A)
    for i in range(1, Q):
        S[i] = S[i-1] + (C[i] - B[i]) * A.count(B[i])
    for i in range(Q):
        print(S[i])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = [0] * Q
    C = [0] * Q
    for i in range(Q):
        B[i], C[i] = map(int, input().split())
    ans = [0] * Q
    ans[0] = sum(A)
    for i in range(1, Q):
        ans[i] = ans[i-1] + (C[i] - B[i]) * A.count(B[i])
    for i in range(Q):
        print(ans[i])

main()

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for i in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    sum_a = sum(A)
    for i in range(Q):
        count = A.count(B[i])
        sum_a += count * (C[i] - B[i])
        print(sum_a)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for i in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    S = sum(A)
    for i in range(Q):
        S += A.count(B[i])*(C[i]-B[i])
        print(S)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for i in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    S = sum(A)
    for i in range(Q):
        S -= A.count(B[i]) * B[i]
        S += A.count(B[i]) * C[i]
        print(S)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for _ in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    ans = sum(A)
    for i in range(Q):
        ans += A.count(B[i]) * (C[i] - B[i])
        print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    Q = int(input())
    B = [0] * Q
    C = [0] * Q
    for i in range(Q):
        B[i], C[i] = [int(i) for i in input().split()]
    S = sum(A)
    for i in range(Q):
        S += (C[i] - B[i]) * A.count(B[i])
        print(S)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    BC = [list(map(int,input().split())) for _ in range(Q)]
    B = [BC[i][0] for i in range(Q)]
    C = [BC[i][1] for i in range(Q)]
    S = [0 for _ in range(Q)]
    #print(N,A,Q,B,C,S)
    for i in range(Q):
        S[i] = sum(A)
        for j in range(N):
            if A[j] == B[i]:
                A[j] = C[i]
                S[i] = S[i] - B[i] + C[i]
        print(S[i])
    return

=======
Suggestion 10

def main():
    #N
    N = int(input())
    #A
    A = list(map(int, input().split()))
    #Q
    Q = int(input())
    #B C
    B = [0]*Q
    C = [0]*Q
    for i in range(Q):
        B[i], C[i] = map(int, input().split())
    #Aの合計値
    Asum = sum(A)
    #Bの合計値
    Bsum = [0]*Q
    #Cの合計値
    Csum = [0]*Q
    #Bsumを求める
    for i in range(Q):
        Bsum[i] = B[i]*(A.count(B[i]))
    #Csumを求める
    for i in range(Q):
        Csum[i] = C[i]*(A.count(B[i]))
    #出力
    for i in range(Q):
        Asum = Asum - Bsum[i] + Csum[i]
        print(Asum)
