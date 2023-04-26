Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (i+j) % 2 == 0 and N-A >= i-A and N-B >= j-B:
                print("#", end="")
            elif (i+j) % 2 == 1 and N-A >= i-A and B-1 >= j-B:
                print("#", end="")
            else:
                print(".", end="")
        print()

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (i + j - A - B) % 2 == 0 and (i - A) * (i - A) + (j - B) * (j - B) <= N * N:
                print('#', end='')
            else:
                print('.', end='')
        print()

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (i <= A + B - j <= N) or (i >= A + B - j >= N+1):
                print('#', end='')
            else:
                print('.', end='')
        print()

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (A <= i <= B) and (A <= j <= B):
                print("#", end="")
            elif (A <= i+j-N-1 <= B) and (A <= j-i+N-1 <= B):
                print("#", end="")
            else:
                print(".", end="")
        print()

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    #print(N, A, B)
    #print(P, Q, R, S)
    for i in range(P, Q+1):
        for j in range(R, S+1):
            ans = 0
            if i >= A and j >= B:
                ans += min(N-i+1, N-j+1)
            if i >= A and j <= B:
                ans += min(N-i+1, j)
            if i <= A and j >= B:
                ans += min(i, N-j+1)
            if i <= A and j <= B:
                ans += min(i, j)
            if ans % 2 == 0:
                print('.', end='')
            else:
                print('#', end='')
        print()

=======
Suggestion 6

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    ans = [["." for _ in range(S - R + 1)] for _ in range(Q - P + 1)]
    for i in range(P, Q + 1):
        for j in range(R, S + 1):
            if (i + j) % 2 == 0:
                continue
            if 1 - A <= i - A <= min(N - A, B - 1):
                ans[i - P][j - R] = "#"
            if 1 - A <= i - A <= min(N - A, N - B):
                ans[i - P][j - R] = "#"
    for i in range(Q - P + 1):
        print("".join(ans[i]))

=======
Suggestion 7

def main():
    #入力
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    #黒マスの数を求める
    #黒マスの数 = 黒マスの数A + 黒マスの数B - 重複する黒マスの数
    #黒マスの数A = (min(N-A,N-B)+1) * (min(N-A,N-B)+2) // 2
    #黒マスの数B = (min(N-A,N-B)+1) * (min(N-A,N-B)+2) // 2
    #重複する黒マスの数 = (min(N-A,N-B)+1) * (min(N-A,N-B)+2) // 2
    #黒マスの数 = (min(N-A,N-B)+1) * (min(N-A,N-B)+2) // 2 * 2
    #黒マスの数 = (min(N-A,N-B)+1) * (min(N-A,N-B)+2) * (min(N-A,N-B)+3) // 6
    #黒マスの数 = (min(N-A,N-B)+1) * (min(N-A,N-B)+2) * (min(N-A,N-B)+3) * (min(N-A,N-B)+4) // 24
    #黒マスの数 = (min(N-A,N-B)+1) * (min(N-A,N-B)+2) * (min(N-A,N-B)+3) * (min(N-A,N-B)+4) * (min(N-A,N-B)+5) // 120
    #黒マスの数 = (min(N-A,N-B)+1) * (min(N-A,N-B)+2) * (min(N-A,N-B)+3) * (min(N-A,N-B)+4) * (min(N-A,N-B)+5) * (min(N-A,N-B)+6) // 720
    #黒マスの数 = (min(N-A,N-B)+1) * (min(N-A,N-B)+2) * (min(N-A,N-B)+3) * (min(N-A,N-B)+

=======
Suggestion 8

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())

    # 1行目の出力
    for j in range(R, S+1):
        if A <= j <= B:
            print('#', end='')
        else:
            print('.', end='')
    print()

    # 2行目以降の出力
    for i in range(P+1, Q+1):
        # 1列目の出力
        if A <= i <= B:
            print('#', end='')
        else:
            print('.', end='')

        # 2列目以降の出力
        for j in range(R+1, S+1):
            if (A <= i <= B) and (A <= j <= B):
                print('#', end='')
            else:
                print('.', end='')
        print()

=======
Suggestion 9

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())

    # 1 つめの操作で塗る黒マスの数を求める
    # 上下左右の端点から塗るマスの数を求める
    # 端点の座標は (A, B) とする
    # 上端点から塗るマスの数を求める
    # max(1-A, 1-B) <= k <= min(N-A, N-B)
    # 上端点から塗るマスの数
    # (N-B) - max(1-A, 1-B) + 1
    # 下端点から塗るマスの数
    # (N-A) - max(1-B, 1-A) + 1
    # 左端点から塗るマスの数
    # (N-A) - max(1-B, 1-A) + 1
    # 右端点から塗るマスの数
    # (N-B) - max(1-A, 1-B) + 1

    # 上端点から塗るマスの数
    tate = min(N-B, N-A) - max(1-A, 1-B) + 1
    # 下端点から塗るマスの数
    yoko = min(N-A, N-B) - max(1-B, 1-A) + 1
    # 1 つめの操作で塗るマスの数
    cnt1 = tate * yoko

    # 2 つめの操作で塗る黒マスの数を求める
    # 上下左右の端点から塗るマスの数を求める
    # 端点の座標は (A, B) とする
    # 上端点から塗るマスの数を求める
    # max(1-A, B-N) <= k <= min(N-A, B-1)
    # 上端点から塗るマ

=======
Suggestion 10

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())

    # 1. (1,1)から(A,B)までの黒のマスの数を求める
    # 2. (1,1)から(A,B)までの白のマスの数を求める
    # 3. (1,1)から(P-1,Q-1)までの黒のマスの数を求める
    # 4. (1,1)から(P-1,Q-1)までの白のマスの数を求める
    # 5. (1,1)から(P-1,R-1)までの黒のマスの数を求める
    # 6. (1,1)から(P-1,R-1)までの白のマスの数を求める
    # 7. (1,1)から(R-1,S-1)までの黒のマスの数を求める
    # 8. (1,1)から(R-1,S-1)までの白のマスの数を求める
    # 9. (1,1)から(R-1,Q-1)までの黒のマスの数を求める
    # 10. (1,1)から(R-1,Q-1)までの白のマスの数を求める
    # 11. (1,1)から(P-1,S-1)までの黒のマスの数を求める
    # 12. (1,1)から(P-1,S-1)までの白のマスの数を求める
    # 13. (1,1)から(P-1,Q-1)までの黒のマスの数を求める
    # 14. (1,1)から(P-1,Q-1)までの白のマスの数を求める
    # 15. (1,1)から(P-1
