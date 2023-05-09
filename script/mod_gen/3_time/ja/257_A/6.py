def main():
    N,X = map(int,input().split())
    #print(N,X)
    for i in range(1,N+1):
        if X <= 26*i:
            print(chr(65+N-i))
            break
        else:
            X -= 26*i
    return

if __name__ == '__main__':
    main()