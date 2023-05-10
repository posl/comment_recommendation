def solve():
    N = int(input())
    ans = 0
    for i in range(1, 10**6):
        if (N - i*(i+1)//2) % i == 0 and (N - i*(i+1)//2) // i >= 0:
            ans += 1
    print(ans*2)

if __name__ == '__main__':
    solve()