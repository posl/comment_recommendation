def main():
    K = int(input())
    if K % 2 == 0:
        print(-1)
        return
    else:
        N = 1
        while True:
            if (N * K + 1) % 2 == 0:
                N += 1
            else:
                print(N)
                return

if __name__ == '__main__':
    main()