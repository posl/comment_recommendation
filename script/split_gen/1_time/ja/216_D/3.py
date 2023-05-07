def main():
    N, M = map(int, input().split())
    A = [0] * (N + 1)
    for _ in range(M):
        _, *a = map(int, input().split())
        for x in a:
            A[x] += 1
    print('Yes' if all(x % 2 == 0 for x in A) else 'No')
