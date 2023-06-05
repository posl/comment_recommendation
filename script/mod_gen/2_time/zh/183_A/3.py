def solve():
    N = int(input())
    A = list(map(int, input().split()))
    pos = 0
    max_pos = 0
    for a in A:
        pos += a
        if pos > max_pos:
            max_pos = pos
    print(max_pos)

if __name__ == '__main__':
    solve()