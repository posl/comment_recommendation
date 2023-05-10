def solve():
    n = int(input())
    print(len(bin(n))-3)
solve()

if __name__ == '__main__':
    solve()