def main():
    n = int(input())
    x = 0
    for i in range(n):
        tmp = input().split()
        if tmp[1] == "JPY":
            x += int(tmp[0])
        else:
            x += float(tmp[0]) * 380000.0
    print(x)

if __name__ == '__main__':
    main()