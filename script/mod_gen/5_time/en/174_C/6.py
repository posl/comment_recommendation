def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
    else:
        n = 1
        while True:
            if int('7' * n) % k == 0:
                print(n)
                break
            else:
                n += 1

if __name__ == '__main__':
    main()