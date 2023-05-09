def main():
    x = int(input())
    res = 0
    res += (x // 500) * 1000
    x -= (x // 500) * 500
    res += (x // 5) * 5
    print(res)

if __name__ == '__main__':
    main()