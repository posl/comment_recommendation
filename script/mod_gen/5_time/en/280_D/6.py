def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    else:
        for i in range(1, K+1):
            if (10**i - 1) % K == 0:
                print(i)
                return
main()

if __name__ == '__main__':
    main()