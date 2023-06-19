def main():
    a = raw_input().split()
    for i in range(10):
        a[i] = int(a[i])
    b = [0] * 10
    for i in range(10):
        b[a[i]] = i
    print b[0]

if __name__ == '__main__':
    main()