def main():
    n = int(input())
    count = 0
    for i in range(1, n):
        for j in range(1, n):
            if n - i * j > 0:
                count += 1
            else:
                break
    print(count)

if __name__ == '__main__':
    main()