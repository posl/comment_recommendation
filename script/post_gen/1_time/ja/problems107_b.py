Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    A = list(map(list, zip(*A)))
    A = list(filter(lambda x: '#' in x, A))
    A = list(map(list, zip(*A)))
    for a in A:
        print(''.join(a))

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    for i in range(H):
        if "#" in A[i]:
            break
    else:
        print()
        exit()

    for i in range(i, H):
        for j in range(W):
            if A[i][j] == "#":
                break
        else:
            continue
        print("".join(A[i][j:]))

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    for i in range(H):
        if "#" in a[i]:
            continue
        a[i] = ""
    for j in range(W):
        if "#" in [a[i][j] for i in range(H)]:
            continue
        for i in range(H):
            a[i] = a[i][:j] + a[i][j+1:]
    for i in range(H):
        print(a[i])

=======
Suggestion 4

def main():
    #入力
    H, W = map(int, input().split())
    a = [input() for i in range(H)]
    #a = [list(map(int, input().split())) for i in range(H)]

    #処理
    #行列の転置
    a = list(map(list, zip(*a)))
    #print(a)

    #行列の転置
    a = list(map(list, zip(*a)))
    #print(a)

    #出力
    for i in range(H):
        for j in range(W):
            print(a[i][j], end="")
        print("")

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    a = list(map(list, zip(*a))) # 行列の転置
    a = [list(filter(lambda x: x != ".", x)) for x in a] # 行ごとに . を除去
    a = list(filter(lambda x: x != [], a)) # 空の行を除去
    a = list(map(list, zip(*a))) # 行列の転置
    a = [list(filter(lambda x: x != ".", x)) for x in a] # 行ごとに . を除去
    a = list(filter(lambda x: x != [], a)) # 空の行を除去
    for i in a:
        print("".join(i))

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    #print(H, W)
    #print(S)

    #行ごとに処理
    for i in range(H):
        #print(S[i])
        if "#" in S[i]:
            #print("Yes")
            continue
        else:
            #print("No")
            S[i] = "."

    #列ごとに処理
    for i in range(W):
        #print(S[i])
        if "#" in S[i]:
            #print("Yes")
            continue
        else:
            #print("No")
            S[i] = "."

    #print(S)
    for i in range(H):
        print(S[i])

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    #print(A)
    #print(H, W)
    #print(A)
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    
    #print(A[0][0])
    #print(A[0][1])
    #print(A[0][2])
    #print(A[0][3])
    #print(A[0][4])
    #print(A[0][5])
    
    #print(A[1][0])
    #print(A[1][1])
    #print(A[1][2])
    #print(A[1][3])
    #print(A[1][4])
    #print(A[1][5])
    
    #print(A[2][0])
    #print(A[2][1])
    #print(A[2][2])
    #print(A[2][3])
    #print(A[2][4])
    #print(A[2][5])
    
    #print(A[3][0])
    #print(A[3][1])
    #print(A[3][2])
    #print(A[3][3])
    #print(A[3][4])
    #print(A[3][5])
    
    #print(A[4][0])
    #print(A[4][1])
    #print(A[4][2])
    #print(A[4][3])
    #print(A[4][4])
    #print(A[4][5])
    
    #print(A[5][0])
    #print(A[5][1])
    #print(A[5][2])
    #print(A[5][3])
    #print(A[5][4])
    #print(A[5][5])
    
    #print(A[6][0])
    #print(A[6][1])
    #print(A[6][2])
    #print(A[6][3])
    #print(A[6][4])
    #print(A[6][5])
    
    #print(A[7][0])
    #print(A[7][1])
    #print(A[7][2])
    #print(A[7][3])
    #print(A[7

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    #print(A)

    # まずは、行ごとに黒いマスがあるかどうかを調べる
    # 黒いマスがある場合、その行は出力対象とする
    # なお、黒いマスがない場合は、その行は出力対象にしない
    for i in range(H):
        if '#' in A[i]:
            print(A[i])

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]

    # 1. 行と列の削除フラグを用意
    # 2. 行と列を削除
    # 3. 行と列の削除フラグによって、削除する行と列を削除
    # 4. 2. 3. を繰り返す
    # 5. マス目を出力

    # 1. 行と列の削除フラグを用意
    # 1.1. 行の削除フラグ
    row_delete = [True] * H
    # 1.2. 列の削除フラグ
    col_delete = [True] * W

    # 2. 行と列を削除
    # 2.1. 行を削除
    for i in range(H):
        if "#" not in a[i]:
            row_delete[i] = False
    # 2.2. 列を削除
    for j in range(W):
        if "#" not in [a[i][j] for i in range(H)]:
            col_delete[j] = False

    # 3. 行と列の削除フラグによって、削除する行と列を削除
    # 3.1. 行を削除
    for i in range(H):
        if not row_delete[i]:
            a[i] = ""
    # 3.2. 列を削除
    for j in range(W):
        if not col_delete[j]:
            for i in range(H):
                a[i] = a[i][:j] + a[i][j+1:]

    # 4. 2. 3. を繰り返す
    # 4.1. 行の削除フラグ
    row_delete = [True] * H
    # 4.2. 列の削除フラグ
    col_delete = [True] * W
    # 4.3. 行を

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]

    # 行方向
    B = [list(map(lambda s: 1 if s == '.' else 0, a)) for a in A]
    for i in range(H):
        if sum(B[i]) == 0:
            B[i] = None
    B = list(filter(lambda b: b is not None, B))

    # 列方向
    C = [[b[i] for b in B] for i in range(len(B[0]))]
    for i in range(len(C)):
        if sum(C[i]) == 0:
            C[i] = None
    C = list(filter(lambda c: c is not None, C))

    # 行方向
    D = [[c[i] for c in C] for i in range(len(C[0]))]

    for d in D:
        print(''.join(list(map(lambda s: '.' if s == 1 else '#', d))))
