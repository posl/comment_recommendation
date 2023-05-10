def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
        return
    P = list(map(int, input().split()))
    for i in range(0, X+1):
        if X-i not in P:
            print(X-i)
            return
        if X+i not in P:
            print(X+i)
            return
