def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 1. B_1 + B_2 + ... + B_N の最大値を求めてください。
    # 2. B_1 + B_2 + ... + B_N の最小値を求めてください。
    # 1. B_1 + B_2 + ... + B_N の最大値を求めてください。
    B = [0] * N
    for i in range(N):
        if i % 2 == 0:
            B[i] = A[i]
        else:
            B[i] = -A[i]
    print(sum(B))
    # 2. B_1 + B_2 + ... + B_N の最小値を求めてください。
    B = [0] * N
    for i in range(N):
        if i % 2 == 0:
            B[i] = -A[i]
        else:
            B[i] = A[i]
    print(sum(B))
