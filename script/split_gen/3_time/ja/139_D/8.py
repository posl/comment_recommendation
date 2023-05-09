def main():
    N = int(input())
    M = [0] * N
    for i in range(1, N + 1):
        M[i - 1] = i % N
    print(sum(M))
