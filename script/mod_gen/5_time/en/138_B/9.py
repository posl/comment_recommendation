def solve():
    n = int(input())
    a = list(map(int, input().split()))
    print(1 / sum([1 / x for x in a]))

if __name__ == '__main__':
    solve()