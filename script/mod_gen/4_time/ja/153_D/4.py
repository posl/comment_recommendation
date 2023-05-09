def solve():
    H = int(input())
    cnt = 0
    while H > 0:
        H = H // 2
        cnt += 1
    print(2 ** cnt - 1)

if __name__ == '__main__':
    solve()