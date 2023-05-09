def main():
    n = int(input())
    for i in range(n, n * n + 1, n):
        if i % 2 == 0:
            print(i)
            break

if __name__ == '__main__':
    main()