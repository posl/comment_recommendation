def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    p = 0
    s = [0, 0, 0, 0]
    for i in range(n):
        s[0] += 1
        for j in range(4):
            if s[j] > 0:
                if j + a[i] >= 4:
                    p += s[j]
                    s[j] = 0
                else:
                    s[j + a[i]] += s[j]
                    s[j] = 0
    print(p)

if __name__ == '__main__':
    main()