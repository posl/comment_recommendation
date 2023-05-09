def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] + x[1])
    
    ans = 0
    for a, b in AB:
        ans += a
        X -= 1
        if X == 0:
            break
    if X > 0:
        ans += X * AB[-1][0] + X * AB[-1][1]
    print(ans)
