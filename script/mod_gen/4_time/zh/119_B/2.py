def main():
    n = int(input())
    y = 0
    for i in range(n):
        x, u = input().split()
        if u == 'JPY':
            y += int(x)
        else:
            y += float(x) * 380000.0
    print(y)

if __name__ == '__main__':
    main()