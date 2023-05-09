def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    #print(X)
    diff = []
    for i in range(M-1):
        diff.append(abs(X[i]-X[i+1]))
    #print(diff)
    diff.sort()
    #print(diff)
    if N >= M:
        print(0)
    else:
        print(sum(diff[:M-N]))

if __name__ == '__main__':
    main()