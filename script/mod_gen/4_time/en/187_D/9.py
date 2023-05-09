def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        tmp = input().split(" ")
        a.append(int(tmp[0]))
        b.append(int(tmp[1]))
    t = 0
    for i in range(n):
        t += a[i]
    t = t/2
    c = 0
    for i in range(n):
        if t < b[i]:
            c += 1
    print(c)

if __name__ == '__main__':
    main()