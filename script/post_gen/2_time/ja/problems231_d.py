Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = "Yes"
    # ここに処理を書く
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(N, M)
    #print(A)
    #print(B)

    #条件を満たす並べ方が存在するなら Yes、存在しないなら No と出力せよ。
    #条件：人 A_i と人 B_i は隣り合っている
    #A_i < B_i
    #A_i < N
    #B_i > 1
    #A_i = i
    #B_i = i+1
    #A_i < B_i

    #A_i < B_i
    #A_i < N
    #B_i > 1
    #A_i = i
    #B_i = i+1
    #A_i < B_i

    #A_i < B_i
    #A_i < N
    #B_i > 1
    #A_i = i
    #B_i = i+1
    #A_i < B_i

    #A_i < B_i
    #A_i < N
    #B_i > 1
    #A_i = i
    #B_i = i+1
    #A_i < B_i

    #A_i < B_i
    #A_i < N
    #B_i > 1
    #A_i = i
    #B_i = i+1
    #A_i < B_i

    #A_i < B_i
    #A_i < N
    #B_i > 1
    #A_i = i
    #B_i = i+1
    #A_i < B_i

    #A_i < B_i
    #A_i < N
    #B_i > 1
    #A_i = i
    #B_i = i+1
    #A_i < B_i

    #A_i < B_i
    #A_i < N
    #B_i > 1
    #A_i = i
    #B_i = i+1
    #A_i <

=======
Suggestion 3

def main():
    N,M = map(int,input().split())
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i],B[i] = map(int,input().split())
    ans = "Yes"
    for i in range(M):
        for j in range(M):
            if A[i] == B[j]:
                ans = "No"
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        edge[A-1].append(B-1)
        edge[B-1].append(A-1)

    ans = "Yes"
    for i in range(N):
        for j in edge[i]:
            for k in edge[j]:
                if i in edge[k]:
                    ans = "No"
                    break

    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    if N == 2 and M == 0:
        print("Yes")
        return

    if N == 2 and M != 0:
        print("No")
        return

    if M == 0:
        print("Yes")
        return

    AB.sort(key=lambda x: x[0])

    # print(AB)

    for i in range(M-1):
        if AB[i][1] == AB[i+1][1]:
            print("No")
            return

    print("Yes")

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    if M == 0:
        print("Yes")
        return
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    last = AB[0][1]
    for i in range(1, M):
        if AB[i][0] < last:
            print("No")
            return
        last = AB[i][1]
    print("Yes")

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    for i in range(M):
        A, B = map(int, input().split())
        if A == 1:
            if B == N:
                print('No')
                return
        elif A == N:
            if B == 1:
                print('No')
                return
    print('Yes')

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    P = [i for i in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        a = P[a]
        b = P[b]
        if a > b:
            a, b = b, a
        P[a] = b
        P[b] = b
    for i in range(1, N + 1):
        if P[i] != P[i + 1]:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])

    # 1人目は必ず1番目に並ぶ
    # 2人目は必ず2番目に並ぶ
    # 3人目は必ず3番目に並ぶ
    # 4人目は必ず4番目に並ぶ
    # という順番で並ぶことができるかどうかを判定する
    # この順番で並べることができるのは、
    # 1番目の人は、3人目の人の隣り合っている人である必要がある
    # 2番目の人は、4人目の人の隣り合っている人である必要がある
    # 3番目の人は、1人目の人の隣り合っている人である必要がある
    # 4番目の人は、2人目の人の隣り合っている人である必要がある
    # という条件を満たすように並べることができるときである
    # 3番目の人は、1人目の人の隣り合っている人である必要がある
    # という条件は、1番目の人が3人目の人の隣り合っている人であることを意味する
    # 4番目の人は、2人目の人の隣り合っている人である必要がある
    # という条件は、2番目の人が4人目の人の隣り合っている人であることを意味する
    # ということは、1番目の人が3人目の人の

=======
Suggestion 10

def main():
    N, M = map(int, input().split())

    # 隣り合っている人を記録するリスト
    # 例えば、1と3が隣り合っているなら、[1,3]と[3,1]の両方を記録する
    neighbor = []

    # 1からNまでのリスト
    num = [i for i in range(1, N+1)]

    for i in range(M):
        A, B = map(int, input().split())
        neighbor.append([A, B])
        neighbor.append([B, A])

    # 隣り合っている人を順番に取り出す
    for i in range(len(neighbor)):
        # 隣り合っている人の位置を取得
        pos1 = num.index(neighbor[i][0])
        pos2 = num.index(neighbor[i][1])

        # 位置が隣り合っていない場合はNoを出力して終了
        if abs(pos1 - pos2) != 1:
            print('No')
            return

    # 隣り合っている人の位置が隣り合っている場合はYesを出力
    print('Yes')
