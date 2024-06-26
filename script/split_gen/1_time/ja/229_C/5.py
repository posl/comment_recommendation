def main():
    N, W = map(int, input().split())
    cheese = []
    for i in range(N):
        cheese.append(list(map(int, input().split())))
    cheese = sorted(cheese, key=lambda x: x[0] / x[1])
    ans = 0
    for i in range(N):
        if cheese[i][1] <= W:
            ans += cheese[i][0]
            W -= cheese[i][1]
        else:
            ans += cheese[i][0] * W / cheese[i][1]
            break
    print(int(ans))
