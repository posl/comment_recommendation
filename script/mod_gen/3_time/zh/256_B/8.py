def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    s = [0, 0, 0, 0]
    for i in range(n):
        s[a[i] - 1] += 1
        p += s[3]
        s[3] = s[2]
        s[2] = s[1]
        s[1] = s[0]
        s[0] = 0
    print(p)

if __name__ == '__main__':
    main()