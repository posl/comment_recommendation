def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
        return
    else:
        i = 1
        n = 7
        while n % k != 0:
            n = (n * 10 + 7) % k
            i += 1
        print(i)

if __name__ == '__main__':
    main()