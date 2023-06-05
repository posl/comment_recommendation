def main():
    X = input()
    M = int(input())
    d = max([int(x) for x in X])
    n = d + 1
    while True:
        if int(X, n) > M:
            print(n - d - 1)
            break
        n += 1
