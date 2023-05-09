def main():
    K, X = map(int, input().split())
    for i in range(K):
        print(X - K + i + 1, end=' ')
    print()
