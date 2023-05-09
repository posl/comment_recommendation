def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    n = 1
    for i in range(1, K + 1):
        n = (n * 10 + 7) % K
        if n == 0:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()