def main():
    N, K = map(int, input().split())
    print(N%K if N%K<K else abs(N%K-K))
