def main():
    N = int(input())
    if N < 1000:
        print(0)
    else:
        count = 0
        for i in range(4, 17, 3):
            if N >= 10 ** i:
                count += (N - 10 ** i + 1)
        print(count)

if __name__ == '__main__':
    main()