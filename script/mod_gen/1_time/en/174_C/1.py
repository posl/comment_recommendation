def main():
    K = int(input())
    if K % 2 == 0:
        print(-1)
        return
    else:
        n = 7 % K
        i = 1
        while n != 0:
            n = (n * 10 + 7) % K
            i += 1
        print(i)
        return

if __name__ == '__main__':
    main()