def main():
    K = int(input())
    if K % 2 == 0:
        print(-1)
        return
    elif K == 1:
        print(1)
        return
    elif K == 3:
        print(3)
        return
    else:
        N = K
        while True:
            N += 2
            if N % 5 == 0:
                continue
            elif N % 3 == 0:
                continue
            elif N % 7 == 0:
                continue
            elif N % K == 0:
                print(N)
                return
            else:
                continue

if __name__ == '__main__':
    main()