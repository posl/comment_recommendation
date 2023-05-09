def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    cnt = 0
    for a, b in AB:
        if a <= b:
            b -= a
            cnt += 1
            if b <= 0:
                break
        else:
            cnt += 1
            break
    print(cnt)

if __name__ == '__main__':
    solve()