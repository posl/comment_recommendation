def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    diff = []
    for i in range(M-1):
        diff.append(abs(X[i+1]-X[i]))
    diff.sort(reverse=True)
    print(sum(diff[N-1:]))

if __name__ == '__main__':
    main()