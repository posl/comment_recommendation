Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    k = [0] * M
    A = [0] * M
    for i in range(M):
        k[i] = int(input())
        A[i] = list(map(int, input().split()))
    #print(N, M)
    #print(k)
    #print(A)
    for i in range(M):
        #print(A[i])
        for j in range(k[i]):
            #print(A[i][j])
            if A[i][j] == 0:
                continue
            for l in range(M):
                if i == l:
                    continue
                for m in range(k[l]):
                    if A[i][j] == A[l][m]:
                        A[i][j] = 0
                        A[l][m] = 0
                        break
    #print(A)
    for i in range(M):
        for j in range(k[i]):
            if A[i][j] != 0:
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    K = [A[i][0] for i in range(M)]
    B = [A[i][1:] for i in range(M)]
    #print(N, M, A, K, B)
    C = [0] * N
    for i in range(M):
        for j in range(K[i]):
            C[B[i][j] - 1] += 1
    #print(C)
    for i in range(N):
        if C[i] % 2 != 0:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = []
    for _ in range(M):
        k = int(input())
        a = list(map(int, input().split()))
        A.append(a)
    #print(N, M)
    #print(A)
    #print(A[0][0])

    # 2N 個のボールがあります。各ボールには 1 以上 N 以下の整数によって表される色が塗られており、各色で塗られたボールはちょうど 2 個ずつ存在します。
    #これらのボールが、底が地面と平行になるように置かれた M 本の筒に入れられています。はじめ、i  (1 ≦ i ≦ M) 本目の筒には k_i 個のボールが入っており、上から j  (1 ≦ j ≦ k_i) 番目のボールの色は a_{i, j} です。
    #あなたの目標は、以下の操作を繰り返すことで M 本の筒全てを空にすることです。
    #異なる 2 本の空でない筒を選び、それぞれの筒の一番上にあるボールを取り出して捨てる。ここで、取り出して捨てた 2 つのボールは同じ色で塗られている必要がある。
    #目標が達成可能かを判定してください。

    # 各色で塗られたボールはちょうど 2 個ずつ存在します。
    # 1 ≦ i ≦ M かつ 1 ≦ j ≦ k_i かつ a_{i,j}=x なる整数の組 (i,j) はちょうど 2 つ存在する
    #

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    k = list()
    a = list()
    for i in range(M):
        k.append(int(input()))
        a.append(list(map(int, input().split())))
    for i in range(M):
        for j in range(k[i]):
            a[i][j] -= 1
    ball = [0] * N
    for i in range(M):
        for j in range(k[i]):
            ball[a[i][j]] += 1
    for i in range(N):
        if ball[i] % 2 == 1:
            print('No')
            return
    print('Yes')

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = [0] * (N + 1)
    for _ in range(M):
        k = int(input())
        for x in map(int, input().split()):
            A[x] += 1
    print('Yes' if all(x % 2 == 0 for x in A) else 'No')

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    balls = [0]*(2*N)
    for i in range(M):
        k = int(input())
        a = list(map(int,input().split()))
        for j in range(k):
            balls[2*i+j] = a[j]
    for i in range(N):
        if balls.count(i+1) != 2:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 7

def main():
    import sys
    from collections import Counter
    input = sys.stdin.buffer.readline
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    B = [Counter(A[i][1:]) for i in range(M)]
    C = Counter()
    for i in range(M):
        for j in B[i]:
            C[j] += B[i][j]
    for i in C:
        if C[i] % 2 == 1:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    A = [[A[i][j] for j in range(1, A[i][0] + 1)] for i in range(M)]
    B = [0 for _ in range(N + 1)]
    for i in range(M):
        for j in range(len(A[i])):
            B[A[i][j]] += 1
    for i in range(1, N + 1):
        if B[i] % 2 == 1:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 9

def main():
    N,M = map(int, input().split())
    k = [0 for i in range(M)]
    a = [[0 for j in range(2*N)] for i in range(M)]
    for i in range(M):
        k[i] = int(input())
        a[i] = list(map(int, input().split()))

    if M == 1:
        print("Yes")
        return

    #aの中身を見ていく
    color = [0 for i in range(N+1)]
    for i in range(M):
        for j in range(k[i]):
            color[a[i][j]] += 1

    #print(color)

    #ボールの個数が奇数ならNo
    for i in range(1,N+1):
        if color[i] % 2 == 1:
            print("No")
            return

    #ボールの個数が偶数ならYes
    print("Yes")

=======
Suggestion 10

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    A = defaultdict(int)
    for _ in range(M):
        input()
        for a in map(int, input().split()):
            A[a] += 1
    
    if all(a % 2 == 0 for a in A.values()):
        print('Yes')
    else:
        print('No')
    
    return
