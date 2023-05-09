def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    s = []
    while True:
        s.append(X)
        X = A[X-1]
        if X in s:
            print(len(s))
            break
