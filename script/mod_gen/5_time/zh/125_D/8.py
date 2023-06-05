def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [abs(x) for x in a]
    c = [x for x in a if x < 0]
    if len(c) % 2 == 0:
        print(sum(b))
    else:
        print(sum(b) - 2 * min(b))

if __name__ == '__main__':
    solve()