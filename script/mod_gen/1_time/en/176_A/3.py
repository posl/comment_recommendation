def main():
    N,X,T = input().split()
    N = int(N)
    X = int(X)
    T = int(T)
    if N%X == 0:
        print(int(N/X)*T)
    else:
        print(int(N/X+1)*T)

if __name__ == '__main__':
    main()