def solve():
    k = int(input())
    if k % 2 == 0:
        print(-1)
        return
    s = 0
    for i in range(1, k + 1):
        s = (s * 10 + 7) % k
        if s == 0:
            print(i)
            return
    print(-1)
    return

if __name__ == '__main__':
    solve()