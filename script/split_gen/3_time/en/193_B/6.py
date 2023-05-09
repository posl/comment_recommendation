def main():
    N = int(input())
    shops = []
    for i in range(N):
        A, P, X = map(int, input().split())
        shops.append((A, P, X))
    shops.sort(key=lambda x: x[0])
    ans = -1
    for A, P, X in shops:
        if X - A > 0:
            ans = P
            break
    print(ans)
