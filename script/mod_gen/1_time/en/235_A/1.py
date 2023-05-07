def main():
    a = input()
    b = a[1] + a[2] + a[0]
    c = a[2] + a[0] + a[1]
    print(int(a) + int(b) + int(c))

if __name__ == '__main__':
    main()