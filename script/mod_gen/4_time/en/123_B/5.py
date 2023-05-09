def solve():
    T = [int(input()) for _ in range(5)]
    T.sort()
    if T[4] % 10 == 0:
        print(sum(T))
    else:
        print(sum(T) - (T[4] % 10) + 10)

if __name__ == '__main__':
    solve()