def solve():
    A, B = list(map(int, input().split()))
    if A >= B:
        print(A)
    else:
        print((2*A+B)/(2**0.5))

if __name__ == '__main__':
    solve()