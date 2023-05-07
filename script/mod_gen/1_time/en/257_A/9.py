def main():
    N, X = map(int, input().split())
    #print(N, X)
    for i in range(1, N+1):
        #print(i)
        if X <= 26*i:
            #print(X - 26*(i-1))
            print(chr(X - 26*(i-1) + 64))
            break
        else:
            X = X - 26*i
            #print(X)

if __name__ == '__main__':
    main()