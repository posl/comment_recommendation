def main():
    n = int(input())
    count = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            for k in range(1, j + 1):
                if i * j * k <= n:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()