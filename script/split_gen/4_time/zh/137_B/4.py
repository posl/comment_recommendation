def main():
    K, X = map(int, input().split())
    min = X - (K - 1)
    max = X + (K - 1)
    for i in range(min, max + 1):
        print(i, end=" ")
