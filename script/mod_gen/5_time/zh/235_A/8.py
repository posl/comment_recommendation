def main():
    abc = int(input())
    a = abc // 100
    b = (abc // 10) % 10
    c = abc % 10
    print(abc + 100 * b + 10 * c + 100 * c + 10 * a + b + 100 * a + 10 * c + b)

if __name__ == '__main__':
    main()