def main():
    n = int(input())
    x = 0
    for i in range(n):
        a, b = input().split()
        if b == 'JPY':
            x += int(a)
        else:
            x += float(a) * 380000.0
    print(x)

if __name__ == '__main__':
    main()