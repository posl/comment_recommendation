Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            if A[i][j] == B[0][0]:
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
    return

=======
Suggestion 3

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            flag = True
            for k in range(H2):
                for l in range(W2):
                    if A[i+k][j+l] != B[k][l]:
                        flag = False
            if flag:
                print("Yes")
                return
    print("No")

=======
Suggestion 4

def main():
    H1, W1 = map(int, input().split())
    A = []
    for i in range(H1):
        A.append(list(map(int, input().split())))
    H2, W2 = map(int, input().split())
    B = []
    for i in range(H2):
        B.append(list(map(int, input().split())))

    # 一致させることができるかどうかを判定
    # 一致させることができる場合は Yes を、
    # 一致させることができない場合は No を出力せよ。
    # ジャッジは英小文字と英大文字を厳密に区別することに注意せよ。

    # Aの行を任意に1つ選んで削除する
    # Aの列を任意に1つ選んで削除する

    # 行列Aを行列Bに一致させることができるかどうかを判定
    # 一致させることができる場合は Yes を、
    # 一致させることができない場合は No を出力せよ。
    # ジャッジは英小文字と英大文字を厳密に区別することに注意せよ。

    # 行列Aを行列Bに一致させることができるかどうかを判定
    # 一致させることができる場合は Yes を、
    # 一致させることができない場合は No を出力せよ。
    # ジャッジは英小文字と英大文字を厳密に区別することに注意せよ。

    # 行列Aを行列Bに一致させることができるかどうかを判定
    # 一致させることができる場合は Yes を、
    # 一

=======
Suggestion 5

def main():
    H1, W1 = map(int, input().split())
    A = []
    for i in range(H1):
        A.append(list(map(int, input().split())))
    H2, W2 = map(int, input().split())
    B = []
    for i in range(H2):
        B.append(list(map(int, input().split())))

    for i in range(H1):
        for j in range(W1):
            if A[i][j] == B[0][0]:
                if (i + H2) <= H1 and (j + W2) <= W1:
                    if A[i:i+H2][j:j+W2] == B:
                        print("Yes")
                        return
    print("No")

=======
Suggestion 6

def main():
    # H_1 W_1
    # A_{1, 1} A_{1, 2} ... A_{1, W_1}
    # A_{2, 1} A_{2, 2} ... A_{2, W_1}
    # .
    # .
    # .
    # A_{H_1, 1} A_{H_1, 2} ... A_{H_1, W_1}
    # H_2 W_2
    # B_{1, 1} B_{1, 2} ... B_{1, W_2}
    # B_{2, 1} B_{2, 2} ... B_{2, W_2}
    # .
    # .
    # .
    # B_{H_2, 1} B_{H_2, 2} ... B_{H_2, W_2}

    # H_1 W_1
    # A_{1, 1} A_{1, 2} ... A_{1, W_1}
    # A_{2, 1} A_{2, 2} ... A_{2, W_1}
    # .
    # .
    # .
    # A_{H_1, 1} A_{H_1, 2} ... A_{H_1, W_1}
    H_1, W_1 = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H_1)]

    # H_2 W_2
    # B_{1, 1} B_{1, 2} ... B_{1, W_2}
    # B_{2, 1} B_{2, 2} ... B_{2, W_2}
    # .
    # .
    # .
    # B_{H_2, 1} B_{H_2, 2} ... B_{H_2, W_2}
    H_2, W_2 = map(int, input().split())
    B = [list(map(int, input().split())) for i in range(H_2)]

    # H_1 >= H_2 かつ W_1 >= W_2 でないなら、No
    if

=======
Suggestion 7

def main():
    # H_1 W_1
    # A_{1, 1} A_{1, 2} ... A_{1, W_1}
    # A_{2, 1} A_{2, 2} ... A_{2, W_1}
    # .
    # .
    # .
    # A_{H_1, 1} A_{H_1, 2} ... A_{H_1, W_1}
    # H_2 W_2
    # B_{1, 1} B_{1, 2} ... B_{1, W_2}
    # B_{2, 1} B_{2, 2} ... B_{2, W_2}
    # .
    # .
    # .
    # B_{H_2, 1} B_{H_2, 2} ... B_{H_2, W_2}
    H1, W1 = map(int, input().split())
    A = []
    for _ in range(H1):
        A.append(list(map(int, input().split())))
    H2, W2 = map(int, input().split())
    B = []
    for _ in range(H2):
        B.append(list(map(int, input().split())))

    # 行列 A に対して、下記の 2 つの操作のうちどちらかを行うことができる。
    # A の行を任意に 1 つ選んで削除する。
    # A の列を任意に 1 つ選んで削除する。
    # 行列 A を行列 B に一致させることができるかどうかを判定して下さい。
    # 判定できる場合は Yes を、判定できない場合は No を出力せよ。
    # ジャッジは英小文字と英大文字を厳密に区別することに注意せよ。

    # 1. 行列 A に対して、下記の 2 つの操作のうちどちらかを行うことができる。
    # A の

=======
Suggestion 8

def main():
    import sys
    input = sys.stdin.readline
    H1,W1 = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(H1)]
    H2,W2 = map(int,input().split())
    B = [list(map(int,input().split())) for _ in range(H2)]
    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            for h in range(H2):
                for w in range(W2):
                    if A[i+h][j+w] != B[h][w]:
                        break
                else:
                    continue
                break
            else:
                print('Yes')
                return
    print('No')
