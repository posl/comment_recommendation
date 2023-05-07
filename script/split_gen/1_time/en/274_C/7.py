def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 深さを保持するリスト
    depth = [0] * (2**N+1)
    # 深さを求める
    for i in range(N):
        depth[A[i]] = 1
    for i in range(2, 2**N+1):
        depth[i] = depth[i//2] + 1
    for i in range(1, 2**N+1):
        print(depth[i])
