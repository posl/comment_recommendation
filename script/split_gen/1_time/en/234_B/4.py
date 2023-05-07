def main():
    N = int(input())
    p = []
    for _ in range(N):
        p.append(tuple(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans = max(ans, ((p[i][0]-p[j][0])**2 + (p[i][1]-p[j][1])**2)**0.5)
    print(ans)
