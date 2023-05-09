def main():
    a = list(map(int, input().split()))
    num = 0
    for i in range(3):
        num = a[num]
    print(num)

if __name__ == '__main__':
    main()