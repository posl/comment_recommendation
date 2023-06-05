def main():
    x = int(input())
    money = 100
    count = 0
    while money < x:
        money = int(money * 1.01)
        count += 1
    print(count)

if __name__ == '__main__':
    main()