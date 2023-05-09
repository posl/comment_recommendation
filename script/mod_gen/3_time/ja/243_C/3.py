def main():
    N = int(input())
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'R':
            X[i] = 10**9 - X[i]
        else:
            Y[i] = 10**9 - Y[i]
    X.sort()
    Y.sort()
    for i in range(N-1):
        if X[i] == X[i+1] or Y[i] == Y[i+1]:
            print('Yes')
            exit()
    print('No')

if __name__ == '__main__':
    main()