def main():
    a = input().split()
    b = []
    for i in range(10):
        b.append(int(a[i]))
    c = []
    d = 0
    while True:
        if not b[d] in c:
            c.append(b[d])
        else:
            break
        d = b[d]
    print(d)

if __name__ == '__main__':
    main()