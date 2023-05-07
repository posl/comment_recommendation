def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # はしごの始点・終点をそれぞれリスト化
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i] = AB[i][0]
        B[i] = AB[i][1]
    # はしごの始点・終点をそれぞれソート
    A.sort()
    B.sort()
    # はしごの始点の最大値と終点の最小値の差を出力
    print(B[-1] - A[0])
