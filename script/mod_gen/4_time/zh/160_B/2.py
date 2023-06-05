def main():
    x = int(input())
    a = x // 500
    x -= a * 500
    b = x // 5
    print(a * 1000 + b * 5)

if __name__ == '__main__':
    main()