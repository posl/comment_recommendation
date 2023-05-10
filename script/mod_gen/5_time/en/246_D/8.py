def solve():
    N = int(input())
    if N == 0:
        print(0)
        return
    for a in range(1, 1000000):
        b = int((a**3 + N)**(1/3))
        if a**3 + a**2*b + a*b**2 + b**3 == N:
            print(a**3 + a**2*b + a*b**2 + b**3)
            return
solve()

if __name__ == '__main__':
    solve()