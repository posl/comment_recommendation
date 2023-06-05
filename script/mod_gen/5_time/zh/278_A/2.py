def problem278_a():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(K):
        A.append(0)
        A.pop(0)
    print(*A)

if __name__ == '__main__':
    problem278_a()