def main():
    N,X,T = map(int,input().split())
    if (N % X) == 0:
        print(int(N/X)*T)
    else:
        print((int(N/X)+1)*T)

if __name__ == '__main__':
    main()