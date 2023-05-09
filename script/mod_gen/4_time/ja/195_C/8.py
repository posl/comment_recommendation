def main():
    N = input()
    N = int(N)
    count = 0
    if N < 1000:
        print(0)
    else:
        for i in range(1000, N + 1):
            if i % 1000 == 0:
                count += 1
        print(count)

if __name__ == '__main__':
    main()