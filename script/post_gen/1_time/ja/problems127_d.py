Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * M
    C = [0] * M
    for i in range(M):
        B[i], C[i] = map(int, input().split())
    #print(N, M)
    #print(A)
    #print(B)
    #print(C)
    A.sort(reverse=True)
    C.sort(reverse=True)
    #print(A)
    #print(C)
    ans = 0
    j = 0
    for i in range(N):
        if j < M and A[i] < C[j]:
            ans += C[j]
            B[j] -= 1
            if B[j] == 0:
                j += 1
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * M
    C = [0] * M
    for i in range(M):
        B[i], C[i] = map(int, input().split())

    A.sort()
    C.sort(reverse=True)
    j = 0
    for i in range(N):
        if j < M and A[i] < C[j]:
            A[i] = C[j]
            B[j] -= 1
            if B[j] == 0:
                j += 1
        else:
            break
    print(sum(A))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    C = []
    for _ in range(M):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    A.sort()

    for i in range(M):
        for j in range(B[i]):
            if A[j] < C[i]:
                A[j] = C[i]
            else:
                break
    print(sum(A))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    C = []
    for _ in range(M):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    # A の要素を降順に並び替える
    A.sort(reverse = True)
    # C の要素を降順に並び替える
    C.sort(reverse = True)
    # A の要素を降順に見ていき、C の要素が大きい順に見ていく
    # C の要素が大きい順に見ていくのは、C の要素を降順に並べているから
    # A の要素が大きい順に見ていくのは、A の要素を降順に並べているから
    # A の要素を降順に見ていき、C の要素が大きい順に見ていく
    # C の要素が大きい順に見ていくのは、C の要素を降順に並べているから
    # A の要素が大きい順に見ていくのは、A の要素を降順に並べているから
    # A の要素を降順に見ていき、C の要素が大きい順に見ていく
    # C の要素が大きい順に見ていくのは、C の要素を降順に並べているから
    # A の要素が大きい順に見ていくのは、A の要素を降順に並べているから
    # A の要素を降順に見ていき、C の要素が大きい順に見ていく
    # C の要素が大きい順に見てい

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    C = []
    for i in range(M):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    A.sort()
    B.sort()
    C.sort(reverse=True)
    A = A + [0]*M
    B = B + [0]*N
    C = C + [0]*N
    i = 0
    j = 0
    k = 0
    while i < N and j < M:
        if A[i] < C[j]:
            A[i] = C[j]
            i += 1
            B[k] -= 1
            if B[k] == 0:
                j += 1
                k += 1
        else:
            i += 1
    print(sum(A))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    C = []
    for i in range(M):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    A.sort()
    C.sort(reverse=True)
    # print(A)
    # print(B)
    # print(C)
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] < C[j]:
            A[i] = C[j]
            B[j] -= 1
            if B[j] == 0:
                j += 1
        i += 1
    print(sum(A))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]
    BC.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for i in range(M):
        for j in range(BC[i][0]):
            if A:
                if BC[i][1] > A[0]:
                    ans += BC[i][1]
                    A.pop(0)
                    continue
            ans += BC[i][1]
            break
    ans += sum(A)
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    C = []
    for i in range(M):
        B.append(list(map(int, input().split())))
    for i in range(M):
        C.append(B[i][1])
    C.sort(reverse=True)
    A.sort(reverse=True)
    count = 0
    for i in range(N):
        if count < M:
            if A[i] < C[count]:
                A[i] = C[count]
                count += 1
    print(sum(A))

=======
Suggestion 9

def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    C = []
    for i in range(M):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)

    A.sort()
    C.sort(reverse=True)
    B.sort(reverse=True)

    i = 0
    j = 0
    while i < N and j < M:
        if A[i] < C[j]:
            A[i] = C[j]
            B[j] -= 1
            i += 1
        else:
            j += 1
        if B[j] == 0:
            j += 1

    print(sum(A))

=======
Suggestion 10

def main():
    # 1行目の入力
    N, M = map(int, input().split())
    # 2行目の入力
    A = list(map(int, input().split()))
    # 3行目以降の入力
    B = []
    C = []
    for _ in range(M):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)

    # Aの各要素を大きい順に並べる
    A.sort(reverse=True)
    # Cの各要素を大きい順に並べる
    C.sort(reverse=True)

    # Aの各要素を順番に見ていく
    for i in range(N):
        # A[i]の値がCの最大値より小さければ終了
        if A[i] < C[0]:
            break
        # A[i]の値がCの最大値以上で、Bの最大値が0なら終了
        if B[0] == 0:
            break
        # A[i]の値がCの最大値以上で、Bの最大値が0でないなら、A[i]の値をCの最大値に書き換える
        A[i] = C[0]
        # Bの最大値を1減らす
        B[0] -= 1
        # Bの最大値が0になったら、Bの最大値をBの最大値-1の値に書き換える
        if B[0] == 0:
            B.sort(reverse=True)
        # Cの最大値をCの最大値-1の値に書き換える
        C.sort(reverse=True)

    # Aの各要素の合計を求める
    ans = sum(A)
    # 答えを出力
    print(ans)
