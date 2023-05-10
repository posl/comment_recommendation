def main():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    edges.sort(key=lambda x: x[2])
    ans = 0
    for i in range(n-1):
        ans += edges[i][2] * (i+1) * (n-i-1)
    print(ans)
