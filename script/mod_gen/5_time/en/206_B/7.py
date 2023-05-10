def solve():
    n = int(input())
    x = 0
    for i in range(1, 100000):
        x += i
        if x >= n:
            print(i)
            break

if __name__ == '__main__':
    solve()