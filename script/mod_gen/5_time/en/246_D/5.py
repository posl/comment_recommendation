def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    else:
        for i in range(1, 1000000):
            if i**3 + (i-1)**3 > n:
                print(i-1)
                return

if __name__ == '__main__':
    main()