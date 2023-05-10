def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 1
    bridge = AB[0][1]
    for i in range(1, M):
        if AB[i][0] <= bridge:
            continue
        ans += 1
        bridge = AB[i][1]
    print(ans)
