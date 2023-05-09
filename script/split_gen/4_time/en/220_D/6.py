def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = [0] * 10
    count[A[-1]] = 1
    for i in range(N - 1):
        c = [0] * 10
        for j in range(10):
            c[(j + A[-i - 2]) % 10] += count[j]
            c[(j * A[-i - 2]) % 10] += count[j]
        count = c
    for i in range(10):
        print(count[i] % 998244353)
