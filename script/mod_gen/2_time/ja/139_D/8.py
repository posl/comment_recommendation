def main():
    N = int(input())
    M = 0
    for i in range(1,N+1):
        M += (N//i) * (i-1) * (N//i)
        if N%i != 0:
            M += (N%i) * (N//i)
    print(M)

if __name__ == '__main__':
    main()