def main():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    a[0], a[1] = a[1], a[0]
    a[0], a[2] = a[2], a[0]
    for i in a:
        print(i, end=' ')

if __name__ == '__main__':
    main()