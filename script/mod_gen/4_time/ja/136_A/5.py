def solve():
    a, b, c = map(int, input().split())
    print(max(0, c-(a-b)))

if __name__ == '__main__':
    solve()