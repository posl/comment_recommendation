def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
    else:
        i = 1
        x = 7
        while x % k != 0:
            x = x * 10 + 7
            x = x % k
            i += 1
        print(i)

if __name__ == '__main__':
    main()