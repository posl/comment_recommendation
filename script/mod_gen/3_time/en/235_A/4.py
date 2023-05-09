def main():
    abc = int(input())
    a = abc // 100
    b = abc % 100 // 10
    c = abc % 10
    print(abc + b * 100 + c * 10 + a)

if __name__ == '__main__':
    main()