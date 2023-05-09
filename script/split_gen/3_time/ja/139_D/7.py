def main():
    N = int(input())
    M = [0 for i in range(N)]
    for i in range(1, N):
        M[i] = N // i * (N // i - 1) // 2 * i
        M[i] += (N % i + 1) * (N // i)
    print(sum(M))
