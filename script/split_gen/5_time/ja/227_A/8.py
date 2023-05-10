def main():
    N, K, A = map(int, input().split())
    if K <= N:
        print(K + A - 1)
    else:
        print(K % N + A - 1)
