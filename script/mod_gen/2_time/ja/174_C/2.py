def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    n = 7
    for i in range(1, K+1):
        if n % K == 0:
            print(i)
            return
        n = (n * 10 + 7) % K

if __name__ == '__main__':
    main()