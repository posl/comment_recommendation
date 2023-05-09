def main():
    n, m = [int(i) for i in input().split()]
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    ans = 0
    for i in s:
        for j in t:
            if i[-3:] == j:
                ans += 1
                break
    print(ans)

if __name__ == '__main__':
    main()