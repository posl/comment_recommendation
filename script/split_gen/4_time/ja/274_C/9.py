def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 親の番号を格納する配列
    parents = [0] * (2 * N + 1)
    for i in range(N):
        parents[A[i]] = i + 1
    # 親を遡っていき、親がいなくなるまでの数を出力する
    for i in range(1, 2 * N + 1):
        p = parents[i]
        cnt = 0
        while p > 0:
            p //= 2
            cnt += 1
        print(cnt)
