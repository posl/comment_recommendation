def main():
    abc = int(input())
    bca = 100 * (abc % 10) + 10 * (abc // 10 % 10) + abc // 100
    cab = 100 * (abc // 100) + 10 * (abc % 10) + abc // 10 % 10
    print(abc + bca + cab)

if __name__ == '__main__':
    main()