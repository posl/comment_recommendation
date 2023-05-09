def main():
    abc = input()
    abc = int(abc)
    a = int(abc / 100)
    b = int(abc / 10) - a * 10
    c = abc - a * 100 - b * 10
    print(a + b + c)

if __name__ == '__main__':
    main()