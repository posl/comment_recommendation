def solve():
    n = int(input())
    s = set()
    for i in range(n):
        si = input()
        if si[0] == '!':
            if si[1:] in s:
                print(si[1:])
                return

if __name__ == '__main__':
    solve()