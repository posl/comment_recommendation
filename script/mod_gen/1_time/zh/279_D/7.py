def solve():
    A,B = map(int,input().split())
    if B >= 1000000000:
        print(A)
    else:
        print(A/((B**2+1)**0.5))

if __name__ == '__main__':
    solve()