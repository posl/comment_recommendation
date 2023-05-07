def main():
    n = int(input())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for a in range(1, 1001):
            for b in range(1, 1001):
                if 4*a*b + 3*a + 3*b == s[i]:
                    break
            else:
                continue
            break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()