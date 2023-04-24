Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 10**18
    for i in range(h):
        for j in range(w):
            ans = min(ans, a[i][j] + c * (i + j), a[i][j] + c * ((h-1-i) + (w-1-j)))
    print(ans)

=======
Suggestion 2

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 10 ** 18
    for i in range(H):
        for j in range(W):
            for a in range(H):
                for b in range(W):
                    if i == a and j == b:
                        continue
                    ans = min(ans, A[i][j] + A[a][b] + C * (abs(i - a) + abs(j - b)))
    print(ans)

=======
Suggestion 3

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 10 ** 18
    for i in range(H):
        for j in range(W):
            for k in range(i, H):
                for l in range(j, W):
                    ans = min(ans, A[i][j] + A[k][l] + C * (abs(i - k) + abs(j - l)))
    print(ans)

=======
Suggestion 4

def main():
    H, W, C = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    B = []
    for i in range(H):
        for j in range(W):
            B.append([A[i][j], i, j])
    B.sort()
    ans = 10**18
    for i in range(H*W):
        for j in range(i+1, H*W):
            ans = min(ans, B[i][0]+B[j][0]+C*(abs(B[i][1]-B[j][1])+abs(B[i][2]-B[j][2])))
    print(ans)
main()

=======
Suggestion 5

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_cost = 10**18
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i == k and j == l:
                        continue
                    min_cost = min(min_cost, A[i][j] + A[k][l] + C * (abs(i-k) + abs(j-l)))
    print(min_cost)

=======
Suggestion 6

def main():
    H, W, C = map(int, input().split())
    A = [[int(x) for x in input().split()] for _ in range(H)]
    ans = 10**18
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i == k and j == l:
                        continue
                    ans = min(ans, A[i][j] + A[k][l] + C*abs(i-k) + C*abs(j-l))
    print(ans)

=======
Suggestion 7

def main():
    H,W,C = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(H)]

    ans = 10**18
    for i in range(H):
        for j in range(W):
            ans = min(ans,A[i][j]+C*i+j)
    for i in range(H):
        for j in range(W):
            ans = min(ans,A[i][j]-C*i-j)
    print(ans)

=======
Suggestion 8

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    # 駅の建設費用の最小値を求める
    B = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if i == j == 0:
                B[i][j] = A[i][j]
            elif i == 0:
                B[i][j] = min(B[i][j - 1], A[i][j])
            elif j == 0:
                B[i][j] = min(B[i - 1][j], A[i][j])
            else:
                B[i][j] = min(B[i - 1][j], B[i][j - 1], A[i][j])

    # 最小値を使って線路の建設費用を求める
    ans = float("inf")
    for i in range(H):
        for j in range(W):
            ans = min(ans, A[i][j] + B[i][j] + C * (i + j))

    print(ans)

=======
Suggestion 9

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    # 1. 2つの異なるマスを選び、それぞれに駅を建設する
    # 2. 建設した 2 つの駅を結ぶ線路を建設する
    # 鉄道建設にかかる費用として考えられる最小値を求める

    # 1. 2つの異なるマスを選び、それぞれに駅を建設する
    # 2. 建設した 2 つの駅を結ぶ線路を建設する
    # 鉄道建設にかかる費用として考えられる最小値を求める

    # 1. 2つの異なるマスを選び、それぞれに駅を建設する
    # 2. 建設した 2 つの駅を結ぶ線路を建設する
    # 鉄道建設にかかる費用として考えられる最小値を求める

    # 1. 2つの異なるマスを選び、それぞれに駅を建設する
    # 2. 建設した 2 つの駅を結ぶ線路を建設する
    # 鉄道建設にかかる費用として考えられる最小値を求める

    # 1. 2つの異なるマスを選び、それぞれに駅を建設する
    # 2. 建設した 2 つの駅を結ぶ線

=======
Suggestion 10

def main():
    import sys
    from functools import reduce
    from operator import mul
    from math import gcd
    def lcm_base(x, y):
        return (x * y) // gcd(x, y)
    def lcm(*numbers):
        return reduce(lcm_base, numbers, 1)
    def lcm_list(numbers):
        return reduce(lcm_base, numbers, 1)
    H, W, C = map(int, input().split())
    A = []
    A.append([0]*(W+1))
    for i in range(H):
        A.append([0]+list(map(int, input().split())))
    #print(A)
    #print(A[1][1])
    #print(A[2][3])
    #print(A[3][3])
    #print(A[1][1] + A[2][3] + C*abs(1-2)+abs(1-3))
    #print(A[1][1] + A[3][3] + C*abs(1-3)+abs(1-3))
    #print(A[2][3] + A[3][3] + C*abs(2-3)+abs(3-3))
    #print(A[1][1] + A[2][3] + C*abs(1-2)+abs(1-3))
    #print(A[1][1] + A[3][3] + C*abs(1-3)+abs(1-3))
    #print(A[2][3] + A[3][3] + C*abs(2-3)+abs(3-3))
    #print(A[1][1] + A[2][3] + C*abs(1-2)+abs(1-3))
    #print(A[1][1] + A[3][3] + C*abs(1-3)+abs(1-3))
    #print(A[2][3] + A[3][3] + C*abs(2-3)+abs(3-3))
    #print(A[1][1] + A[2][3] + C*abs(1-2)+abs(1-3))
    #print(A[1][1] + A[3][3] + C*abs(1-3)+abs(1
