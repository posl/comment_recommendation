def solve():
    A,B = map(int,input().split())
    g = 1
    ans = A/((g) ** (1/2))
    while (1):
        g += 1
        if A/((g) ** (1/2)) <= B * (g-1):
            break
        ans = A/((g) ** (1/2))
    print(ans)
    return 0

if __name__ == '__main__':
    solve()