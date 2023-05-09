def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    s = [0, 0, 0, 0]
    for i in range(n):
        s[0] += 1
        for j in range(4):
            if s[j] > 0:
                s[j] -= 1
                if j + a[i] < 4:
                    s[j + a[i]] += 1
                else:
                    p += 1
    print(p)

if __name__ == '__main__':
    main()