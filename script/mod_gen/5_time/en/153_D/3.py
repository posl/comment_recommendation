def solve():
    h = int(input())
    x = 1
    while True:
        if h == 1:
            return x
        else:
            x = x * 2
            h = h // 2
print(solve())

if __name__ == '__main__':
    solve()