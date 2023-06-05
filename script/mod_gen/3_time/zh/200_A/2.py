def main():
    year = input("请输入年份：")
    year = int(year)
    if year % 100 == 0:
        year = year // 100
    else:
        year = year // 100 + 1
    print(year)

if __name__ == '__main__':
    main()