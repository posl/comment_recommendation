Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            for k in range(H2):
                for l in range(W2):
                    if A[i+k][j+l] != B[k][l]:
                        break
                else:
                    continue
                break
            else:
                print("Yes")
                return
    print("No")

=======
Suggestion 2

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]

    # 1. 行列 A の行を削除
    # 2. 行列 A の列を削除
    # 3. 行列 B の行を削除
    # 4. 行列 B の列を削除
    # 5. 行列 A と行列 B の要素を比較
    # 6. 行列 A の行と行列 B の行を比較
    # 7. 行列 A の列と行列 B の列を比較

    # 1. 行列 A の行を削除
    # 2. 行列 A の列を削除
    # 3. 行列 B の行を削除
    # 4. 行列 B の列を削除
    # 5. 行列 A と行列 B の要素を比較
    # 6. 行列 A の行と行列 B の行を比較
    # 7. 行列 A の列と行列 B の列を比較
    # 8. 行列 A の行と行列 B の列を比較
    # 9. 行列 A の列と行列 B の行を比較

    # 1. 行列 A の行を削除
    # 2. 行列 A の列を削除
    # 3. 行列 B の行を削除
    # 4. 行列 B の列を削除
    # 5. 行列 A と行列 B の要素を比較
    # 6. 行列 A の行と行列 B の行を比較
    # 7. 行列 A の

=======
Suggestion 3

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            if A[i][j] == B[0][0]:
                for k in range(H2):
                    for l in range(W2):
                        if A[i + k][j + l] != B[k][l]:
                            break
                    else:
                        continue
                    break
                else:
                    print("Yes")
                    return
    print("No")

=======
Suggestion 4

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            if A[i][j] == B[0][0]:
                for k in range(H2):
                    for l in range(W2):
                        if A[i + k][j + l] != B[k][l]:
                            break
                    else:
                        continue
                    break
                else:
                    print('Yes')
                    return
    print('No')

=======
Suggestion 5

def main():
    H_1, W_1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H_1)]
    H_2, W_2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H_2)]

    # どこにも適合しないならNO
    for i in range(H_2):
        for j in range(W_2):
            if B[i][j] not in A[i]:
                print("No")
                exit()

    # 一致するならYES
    for i in range(H_2):
        for j in range(W_2):
            if B[i][j] != A[i][j]:
                print("No")
                exit()
    print("Yes")

=======
Suggestion 6

def main():
    H1,W1 = map(int,input().split())
    A = []
    for i in range(H1):
        A.append(list(map(int,input().split())))
    H2,W2 = map(int,input().split())
    B = []
    for i in range(H2):
        B.append(list(map(int,input().split())))
    #print(A)
    #print(B)
    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            flag = True
            for k in range(H2):
                for l in range(W2):
                    if A[i+k][j+l] != B[k][l]:
                        flag = False
            if flag:
                print('Yes')
                return
    print('No')
    return

=======
Suggestion 7

def main():
    # 入力
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]

    # 処理
    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            for k in range(H2):
                for l in range(W2):
                    if A[i+k][j+l] != B[k][l]:
                        break
                else:
                    continue
                break
            else:
                print("Yes")
                return
    else:
        print("No")

=======
Suggestion 8

def main():
    import sys
    input = sys.stdin.readline

    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]

    ans = "Yes"
    for i in range(H1):
        for j in range(W1):
            if i < H2 and j < W2:
                if A[i][j] != B[i][j]:
                    ans = "No"
                    break
            else:
                if A[i][j] != 0:
                    ans = "No"
                    break

    print(ans)

=======
Suggestion 9

def main():
    H1, W1 = map(int, input().split(' '))
    A = []
    for i in range(H1):
        A.append(list(map(int, input().split(' '))))

    H2, W2 = map(int, input().split(' '))
    B = []
    for i in range(H2):
        B.append(list(map(int, input().split(' '))))

    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            if check(A, B, i, j, H2, W2):
                print('Yes')
                return

    print('No')

=======
Suggestion 10

def main():
    # 1行目
    H1, W1 = map(int, input().split())
    # 2行目以降
    A = [list(map(int, input().split())) for _ in range(H1)]
    # 1行目
    H2, W2 = map(int, input().split())
    # 2行目以降
    B = [list(map(int, input().split())) for _ in range(H2)]

    # ここに処理を書く
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            # 切り出し
            C = [A[k][j:j+W2] for k in range(i, i+H2)]
            # 切り出した行列とBが一致するか
            if C == B:
                print('Yes')
                exit()
    print('No')
