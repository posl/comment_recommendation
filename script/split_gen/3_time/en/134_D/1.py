def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0] * N
    for i in range(N - 1, -1, -1):
        if sum(b[i::i + 1]) % 2 != a[i]:
            b[i] = 1
    print(sum(b))
    print(*[i + 1 for i in range(N) if b[i] == 1])
