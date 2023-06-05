def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    ans = 1000000000000000
    for i in range(N):
        for j in range(N):
            if i == j:
                ans = min(ans, AB[i][0] + AB[j][1])
            else:
                ans = min(ans, max(AB[i][0], AB[j][1]))
    print(ans)
