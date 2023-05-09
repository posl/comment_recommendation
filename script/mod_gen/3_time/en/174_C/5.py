def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    else:
        num = 7
        for i in range(1, K + 1):
            if num % K == 0:
                print(i)
                return
            num = num * 10 + 7
        print(-1)

if __name__ == '__main__':
    main()