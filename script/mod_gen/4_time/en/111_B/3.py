def main():
    abc = int(input())
    if abc % 111 == 0:
        print(abc)
    else:
        print((abc // 111 + 1) * 111)

if __name__ == '__main__':
    main()