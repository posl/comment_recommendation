def main():
    X,K = map(int, input().split())
    for i in range(1,K+1):
        if X%(10**i) < 5*(10**(i-1)):
            print((X//(10**i))*(10**i))
            break
        else:
            print((X//(10**i)+1)*(10**i))
            break

if __name__ == '__main__':
    main()