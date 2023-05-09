def problems184_b():
    n, x = map(int, input().split())
    s = input()
    ans = x
    for i in range(n):
        if s[i] == 'o':
            ans += 1
        elif s[i] == 'x':
            if ans > 0:
                ans -= 1
    print(ans)

if __name__ == '__main__':
    problems184_b()