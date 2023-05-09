def solve():
    A, B = map(int, input().split())
    g = 1
    time = A
    while True:
        if time <= B:
            break
        g += 1
        time = (A + time) / 2
    print(time)

if __name__ == '__main__':
    solve()