def main():
    abc = int(input())
    a = abc // 100
    b = abc % 100 // 10
    c = abc % 10
    print((a + b + c) * (a * 100 + b * 10 + c))

if __name__ == '__main__':
    main()