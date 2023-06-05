def solve():
    N = int(input())
    # print(N)
    ans = N
    for i in range(2, int(N**0.5)+1):
        j = 2
        while i**j <= N:
            ans -= 1
            j += 1
    print(ans)

if __name__ == '__main__':
    solve()