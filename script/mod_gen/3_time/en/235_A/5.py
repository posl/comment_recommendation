def main():
    abc = int(input())
    a = abc // 100
    b = abc % 100 // 10
    c = abc % 10
    print(a + b + c + b * 10 + c * 100 + a * 110)

if __name__ == '__main__':
    main()