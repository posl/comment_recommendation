def main():
    N, M = map(int, input().split())
    cake = []
    for _ in range(N):
        cake.append(list(map(int, input().split())))
    ans = 0
    for i in range(8):
        tmp = []
        for j in range(N):
            tmp.append(sum([cake[j][k] * (-1)**(i>>k & 1) for k in range(3)]))
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)
