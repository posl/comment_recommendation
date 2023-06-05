def main():
    n, w = map(int, input().split())
    cheese = []
    for i in range(n):
        cheese.append(list(map(int, input().split())))
    cheese = sorted(cheese, key=lambda x: x[0] / x[1])
    cheese = cheese[::-1]
    ans = 0
    for i in range(n):
        if w <= 0:
            break
        if w >= cheese[i][1]:
            ans += cheese[i][0]
            w -= cheese[i][1]
        else:
            ans += cheese[i][0] * w / cheese[i][1]
            w = 0
    print(int(ans))
