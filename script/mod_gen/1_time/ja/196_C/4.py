def solve():
    N = int(input())
    ans = 0
    for i in range(1, 1000001):
        s = str(i) + str(i)
        if int(s) <= N:
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    solve()