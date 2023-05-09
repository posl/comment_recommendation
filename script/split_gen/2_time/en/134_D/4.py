def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N - 1, -1, -1):
        if sum(B[i::i + 1]) % 2 != A[i]:
            B[i] = 1
    print(sum(B))
    print(*[i + 1 for i, x in enumerate(B) if x])
