def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    diff = []
    for i in range(M-1):
        diff.append(X[i+1]-X[i])
    diff.sort()
    if N >= M:
        print(0)
    else:
        print(sum(diff[:M-N]))

if __name__ == '__main__':
    main()