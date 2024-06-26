def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        return
    diff = [X[i+1] - X[i] for i in range(M-1)]
    diff.sort()
    print(sum(diff[:M-N]))
