def main():
    N = int(input())
    points = [list(map(int,input().split())) for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for k in range(N):
                if i == k or j == k:
                    continue
                for l in range(N):
                    if i == l or j == l or k == l:
                        continue
                    if points[i][0] == points[j][0] and points[k][0] == points[l][0] and points[i][0] != points[k][0] and points[i][1] == points[k][1] and points[j][1] == points[l][1] and points[i][1] != points[j][1]:
                        ans += 1
    print(ans//2)
