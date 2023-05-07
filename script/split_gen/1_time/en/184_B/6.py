def main():
    N, X = [int(x) for x in input().split()]
    S = input()
    for s in S:
        if s == 'o':
            X += 1
        else:
            X = max(0, X-1)
    print(X)
