def main():
    abc = int(input())
    bca = abc * 10 % 1000 + abc // 100
    cab = abc * 100 % 1000 + abc // 10
    print(abc + bca + cab)

if __name__ == '__main__':
    main()