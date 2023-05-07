def main():
    N,M,X,T,D = map(int, input().split())
    if M < X:
        print(T+(M-1)*D)
    else:
        print(T+(X-1)*D+(N-X)*D)

if __name__ == '__main__':
    main()