def main():
    a = input().split()
    sum = 0
    for i in a:
        sum += int(i)
    if sum >= 22:
        print("bust")
    else:
        print("win")

if __name__ == '__main__':
    main()