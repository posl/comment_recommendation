def main():
    x = int(input())
    a = x // 500
    b = x % 500
    c = b // 5
    print(a * 1000 + c * 5)

if __name__ == '__main__':
    main()