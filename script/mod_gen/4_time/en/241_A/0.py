def main():
    a = list(map(int, input().split()))
    b = a[0]
    for i in range(3):
        b = a[b]
    print(b)

if __name__ == '__main__':
    main()