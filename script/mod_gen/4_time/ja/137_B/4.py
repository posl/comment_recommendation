def main():
    K,X = map(int,input().split())
    for i in range(K):
        print(X-K+i+1,end=" ")
    for i in range(K-1):
        print(X+1+i+1,end=" ")
    print(X+K)

if __name__ == '__main__':
    main()