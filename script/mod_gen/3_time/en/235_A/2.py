def main():
    abc = int(input())
    a = abc // 100
    b = (abc % 100) // 10
    c = abc % 10
    bca = b * 100 + c * 10 + a
    cab = c * 100 + a * 10 + b
    print(abc + bca + cab)

if __name__ == '__main__':
    main()