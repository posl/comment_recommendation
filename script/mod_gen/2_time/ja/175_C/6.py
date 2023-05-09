def main():
    X,K,D = map(int,input().split())
    X = abs(X)
    if X//D > K:
        print(X-D*K)
    else:
        if (K-X//D)%2 == 0:
            print(X%D)
        else:
            print(abs(X%D-D))

if __name__ == '__main__':
    main()