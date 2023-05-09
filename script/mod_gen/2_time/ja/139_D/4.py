def main():
    n = int(input())
    if n == 1:
        print(0)
        return
    print(n * (n - 1) // 2)

if __name__ == '__main__':
    main()