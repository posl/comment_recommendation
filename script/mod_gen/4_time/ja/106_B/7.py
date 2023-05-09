def main():
    n = int(input())
    print(sum(1 for i in range(1, n + 1, 2) if 8 == sum(1 for j in range(1, i + 1) if 0 == i % j)))

if __name__ == '__main__':
    main()