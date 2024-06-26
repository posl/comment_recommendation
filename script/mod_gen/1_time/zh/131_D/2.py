def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    time = 0
    for a, b in AB:
        time += a
        if time > b:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    solve()