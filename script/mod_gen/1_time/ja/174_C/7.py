def main():
    K = int(input())
    if K % 2 == 0:
        print(-1)
        return
    else:
        n = 7
        for i in range(1, 10**6):
            if n % K == 0:
                print(i)
                return
            else:
                n = n * 10 + 7
        print(-1)
        return

if __name__ == '__main__':
    main()