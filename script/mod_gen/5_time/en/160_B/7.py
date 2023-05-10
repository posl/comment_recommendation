def main():
    x = int(input())
    n = x // 500
    m = x % 500
    o = m // 5
    print(n*1000 + o*5)

if __name__ == '__main__':
    main()