def main():
    N, X = map(int, input().split())
    AB = []
    for _ in range(N):
        AB.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        ans += AB[i][0] * AB[i][1]
    ans += X * min([AB[i][0] for i in range(N)])
    print(ans)
