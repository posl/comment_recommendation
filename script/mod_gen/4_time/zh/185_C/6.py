def solve():
    L = int(input())
    ans = 0
    for a in range(1, L-10):
        for b in range(1, L-10-a):
            c = L-a-b
            ans += (a+b+c-1)*(a+b+c-2)//2
    print(ans)

if __name__ == '__main__':
    solve()