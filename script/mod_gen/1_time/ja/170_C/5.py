def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
    else:
        P = list(map(int, input().split()))
        #print(X, N, P)
        for i in range(101):
            if X-i not in P:
                print(X-i)
                break
            elif X+i not in P:
                print(X+i)
                break

if __name__ == '__main__':
    main()