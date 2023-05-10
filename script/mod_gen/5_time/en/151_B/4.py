def problem151_b():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(max(0, N*M - sum(A)) if max(0, N*M - sum(A)) <= K else -1)

if __name__ == '__main__':
    problem151_b()