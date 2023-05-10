def main():
    N, M = map(int, input().split())
    X = sorted(list(map(int, input().split())))
    if N >= M:
        print(0)
    else:
        diff = [0] * (M-1)
        for i in range(M-1):
            diff[i] = X[i+1] - X[i]
        diff.sort()
        print(sum(diff[:M-N]))
