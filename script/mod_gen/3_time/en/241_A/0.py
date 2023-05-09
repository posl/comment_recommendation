def main():
    a = list(map(int, input().split()))
    x = 0
    for i in range(3):
        x = a[x]
    print(x)

if __name__ == '__main__':
    main()