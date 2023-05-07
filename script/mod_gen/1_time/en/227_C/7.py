def main():
    n = int(input().strip())
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        for j in range(i, int(n ** 0.5) + 1):
            if i * j > n:
                break
            count += 1
    print(count)

if __name__ == '__main__':
    main()