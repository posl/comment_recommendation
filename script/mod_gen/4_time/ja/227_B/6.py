def solve():
    n = int(input())
    s = list(map(int, input().split()))
    ret = 0
    for i in range(n):
        if s[i] == 1:
            continue
        for j in range(2, s[i]):
            if s[i] % j == 0:
                ret += 1
                break
    print(ret)
    return 0

if __name__ == '__main__':
    solve()