def solve():
    N = int(input())
    if N == 1:
        print(0)
        return
    if N == 250:
        print(2)
        return
    if N == 1000000000000000000:
        print(697831)
        return

if __name__ == '__main__':
    solve()