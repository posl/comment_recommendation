def main():
    x = int(input())
    n = 0
    while x > 100:
        x = x * 101 // 100
        n += 1
    print(n)

if __name__ == '__main__':
    main()