def solve():
    N = int(input())
    C = input()
    R = C.count('R')
    W = C.count('W')
    if R == 0 or W == 0:
        print(0)
        return
    if C[0] == 'R':
        print(C[:R].count('W'))
    else:
        print(C[R:].count('R'))

if __name__ == '__main__':
    solve()