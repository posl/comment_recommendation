def main():
    N,M = map(int,input().split())
    for i in range(1,M+1):
        if N == 1:
            print(i)
        else:
            search(i,i+1,N,M)

if __name__ == '__main__':
    main()