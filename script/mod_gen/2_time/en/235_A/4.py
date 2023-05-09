def main():
    abc = int(input())
    a = abc // 100
    b = abc % 100 // 10
    c = abc % 10
    print(a + b + c + a * 10 + b * 100 + c * 1000 + b * 10 + c * 100 + a * 1000)
main()

if __name__ == '__main__':
    main()