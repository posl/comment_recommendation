def main():
    N, M = map(int, input().split())
    light = []
    for _ in range(M):
        light.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        count = 0
        for j in range(M):
            on = 0
            for k in range(1, light[j][0] + 1):
                if (i >> (light[j][k] - 1)) & 1:
                    on += 1
            if on % 2 == p[j]:
                count += 1
        if count == M:
            ans += 1
    print(ans)
