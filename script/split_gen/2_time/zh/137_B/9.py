def main():
    K, X = map(int, input().split())
    left = X - K + 1
    right = X + K - 1
    for i in range(left, right+1):
        print(i, end=" ")
    print()
