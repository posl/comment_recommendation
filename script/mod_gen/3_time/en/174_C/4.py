def main():
    K = int(input())
    N = 7
    for i in range(1, K+1):
        if N % K == 0:
            print(i)
            break
        N = N * 10 + 7
    else:
        print(-1)

if __name__ == '__main__':
    main()