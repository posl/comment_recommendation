def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    diff = [abs(X[i+1]-X[i]) for i in range(M-1)]
    diff.sort(reverse=True)
    print(sum(diff[N-1:]))
