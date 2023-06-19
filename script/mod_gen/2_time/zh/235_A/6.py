def main():
    abc = int(input())
    a = abc // 100
    b = abc // 10 % 10
    c = abc % 10
    print(a * 111 + b * 111 + c * 111)

if __name__ == '__main__':
    main()