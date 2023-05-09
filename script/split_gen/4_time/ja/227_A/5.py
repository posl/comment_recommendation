def main():
    N, K, A = map(int, input().split())
    result = (K - (N - A + 1)) % N
    print(N if result == 0 else result)
