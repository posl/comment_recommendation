def main():
    abc = int(input())
    bca = abc // 100 + (abc % 100) // 10 * 10 + abc % 10 * 100
    cab = abc % 10 + (abc % 100) // 10 * 10 + abc // 100 * 100
    print(abc + bca + cab)

if __name__ == '__main__':
    main()