Synthesizing 10/10 solutions

=======
Suggestion 1

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

    # 使い方
    # A = [1, 2, 3, 4, 5]
    # B = [1, 3, 5]
    # C = [10, 30, 50]
    # print(replace(A, B, C))
    # [10, 2, 30, 4, 50]
    def replace(A, B, C):
        for i in range(len(B)):
            for j in range(len(A)):
                if A[j] == B[i]:
                    A[j] = C[i]
        return A

    # 使い方
    # A = [1, 2, 3, 4, 5]
    # B = [1, 3, 5]
    # C = [10, 30, 50]
    # print(replace_sum(A, B, C))
    # 110
    def replace_sum(A, B, C):
        sum = 0
        for i in range(len(B)):
            for j in range(len(A)):
                if A[j] == B[i]:
                    A[j] = C[i]
        for i in range(len(A)):
            sum += A[i]
        return sum

    for i in range(Q):
        print(replace_sum(A, B, C))

=======
Suggestion 2

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

    #Bの要素の値をキーとする辞書を作る
    D = {}
    for i in range(N):
        if A[i] in D:
            D[A[i]] += 1
        else:
            D[A[i]] = 1

    sum = 0
    for i in range(N):
        sum += A[i]

    for i in range(Q):
        if B[i] in D:
            sum -= D[B[i]] * B[i]
            sum += D[B[i]] * C[i]
            if C[i] in D:
                D[C[i]] += D[B[i]]
            else:
                D[C[i]] = D[B[i]]
            del D[B[i]]
        print(sum)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B, C = [], []
    for _ in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    ans = [0] * Q
    ans[0] = sum(A)
    for i in range(1, Q):
        ans[i] = ans[i-1] + (C[i] - B[i]) * A.count(B[i])
    for i in range(Q):
        print(ans[i])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for i in range(Q):
        B.append(list(map(int, input().split())))
    for i in range(Q):
        C.append(B[i][1])
    #print(C)
    
    #A = [1, 2, 3, 4]
    #B = [[1, 2], [3, 4], [2, 4]]
    #C = [2, 4, 4]
    #Q = 3
    
    #A = [1, 1, 1, 1]
    #B = [[1, 2], [2, 1], [3, 5]]
    #C = [2, 1, 5]
    #Q = 3
    
    #A = [1, 2]
    #B = [[1, 100], [2, 100], [100, 1000]]
    #C = [100, 100, 1000]
    #Q = 3
    
    #A = [1, 1, 1, 1]
    #B = [[1, 2], [2, 1], [3, 5]]
    #C = [2, 1, 5]
    #Q = 3
    
    #A = [1, 1, 1, 1]
    #B = [[1, 2], [2, 1], [3, 5]]
    #C = [2, 1, 5]
    #Q = 3
    
    #A = [1, 1, 1, 1]
    #B = [[1, 2], [2, 1], [3, 5]]
    #C = [2, 1, 5]
    #Q = 3
    
    #A = [1, 1, 1, 1]
    #B = [[1, 2], [2, 1], [3, 5]]
    #C = [2, 1, 5]
    #Q = 3
    
    #A = [1, 1, 1, 1]
    #B = [[1, 2],

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]

    from collections import Counter
    counter = Counter(A)

    sumA = sum(A)

    for B, C in BC:
        sumA += (C - B) * counter[B]
        counter[C] += counter[B]
        counter[B] = 0
        print(sumA)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    S = [0] * (Q + 1)
    S[0] = sum(A)
    B = [0] * (N + 1)
    for i in range(N):
        B[A[i]] += 1
    for i in range(Q):
        S[i + 1] = S[i] + (BC[i][1] - BC[i][0]) * B[BC[i][0]]
        B[BC[i][1]] += B[BC[i][0]]
        B[BC[i][0]] = 0
    for i in range(Q):
        print(S[i + 1])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, A, Q, BC)
    
    # Aの要素の値がBであるものの個数を記録
    count = [0] * (10**5 + 1)
    for a in A:
        count[a] += 1
    
    # S_{i}を記録
    S = [0] * (Q+1)
    S[0] = sum(A)
    for i in range(Q):
        B, C = BC[i]
        S[i+1] = S[i] - B * count[B] + C * count[B]
        count[C] += count[B]
        count[B] = 0
        print(S[i+1])

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [tuple(map(int, input().split())) for _ in range(Q)]
    ans = [0] * Q
    ans[0] = sum(A)
    B = [0] * (10 ** 5 + 1)
    for a in A:
        B[a] += 1
    for i in range(1, Q):
        b, c = BC[i]
        ans[i] = ans[i - 1] - b * B[b] + c * B[b]
        B[c] += B[b]
        B[b] = 0
    for a in ans:
        print(a)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]

    # 1. Aの値がBの個数を求める
    # 2. Aの値がBの個数をCに置き換える
    # 3. Aの合計を求める
    # 4. Aの合計を出力
    # 5. 1~4をQ回繰り返す

    for i in range(Q):
        # Aの値がBの個数を求める
        count = 0
        for j in range(N):
            if A[j] == BC[i][0]:
                count += 1
        # Aの値がBの個数をCに置き換える
        for j in range(N):
            if A[j] == BC[i][0]:
                A[j] = BC[i][1]
        # Aの合計を求める
        sum = 0
        for j in range(N):
            sum += A[j]
        # Aの合計を出力
        print(sum)

=======
Suggestion 10

def main():
    N=int(input())
    A=list(map(int,input().split()))
    Q=int(input())
    BC=[list(map(int,input().split())) for _ in range(Q)]
    #print(N,A,Q,BC)
    A_sum=sum(A)
    #print(A_sum)
    A_count=[0]*(10**5+1)
    for i in A:
        A_count[i]+=1
    #print(A_count)
    for i in range(Q):
        B,C=BC[i]
        A_sum+=A_count[B]*(C-B)
        A_count[C]+=A_count[B]
        A_count[B]=0
        print(A_sum)
