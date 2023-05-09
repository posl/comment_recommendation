def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    diff = [X[i+1] - X[i] for i in range(M-1)]
    diff.sort()
    print(sum(diff[:max(0, M-N)]))

if __name__ == '__main__':
    main()