def main():
    N,X,Y = map(int,input().split())
    print(N,X,Y)
    for i in range(N-1):
        U,V = map(int,input().split())
        print(U,V)

if __name__ == '__main__':
    main()