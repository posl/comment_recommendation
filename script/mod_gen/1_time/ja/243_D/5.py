def main():
    N,X = map(int,input().split())
    S = input()
    for i in range(N):
        if S[i] == 'U':
            X = X//2
        elif S[i] == 'L':
            X = (X-1)//2
        else:
            X = (X+1)//2
    print(X)

if __name__ == '__main__':
    main()