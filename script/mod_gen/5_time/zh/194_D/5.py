def solve():
    N = int(input())
    print(sum([1/i for i in range(1, N+1)]))

if __name__ == '__main__':
    solve()