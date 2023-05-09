def main():
    N = int(input())
    xyp = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for k in range(N):
                if k == i or k == j:
                    continue
                if xyp[i][2] * (abs(xyp[i][0] - xyp[j][0]) + abs(xyp[i][1] - xyp[j][1])) >= abs(xyp[k][0] - xyp[j][0]) + abs(xyp[k][1] - xyp[j][1]):
                    ans = max(ans, xyp[i][2] * (abs(xyp[i][0] - xyp[j][0]) + abs(xyp[i][1] - xyp[j][1])))
    print(ans)
