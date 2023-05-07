def main():
    n = int(input())
    towns = []
    for i in range(n):
        towns.append(tuple(map(int, input().split())))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            x = towns[i][0] - towns[j][0]
            y = towns[i][1] - towns[j][1]
            ans = max(ans, x*x + y*y)
    print(ans)
