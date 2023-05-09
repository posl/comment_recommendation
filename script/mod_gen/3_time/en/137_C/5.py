def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    d = {}
    for i in s:
        i = ''.join(sorted(i))
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()