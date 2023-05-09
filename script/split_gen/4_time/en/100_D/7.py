def main():
    N, M = map(int, input().split())
    xyz = [list(map(int, input().split())) for _ in range(N)]
    
    ans = 0
    for i in range(8):
        s = 0
        for j in range(N):
            t = 0
            for k in range(3):
                t += xyz[j][k] * (-1)**((i>>k) & 1)
            s += t
        ans = max(ans, abs(s))
    print(ans)
