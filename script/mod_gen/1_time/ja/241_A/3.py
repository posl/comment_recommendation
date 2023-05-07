def main():
    a = input().split()
    for i in range(3):
        a[0] = a[int(a[0])]
    print(a[0])

if __name__ == '__main__':
    main()