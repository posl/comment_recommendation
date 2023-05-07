def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    p.reverse()
    ans = p[0] // 2
    for i in range(1, n):
        ans += p[i]
    print(ans)

if __name__ == '__main__':
    main()