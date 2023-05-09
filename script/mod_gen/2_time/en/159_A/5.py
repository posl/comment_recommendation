def main():
    N, M = map(int, input().split())
    #N = 0 or 1
    if N == 0:
        print(M)
    #N = 1
    elif N == 1:
        print(M*(M-1)//2)
    #N >= 2
    else:
        print(N*M + (N*(N-1)//2)*(M*(M-1)//2))

if __name__ == '__main__':
    main()