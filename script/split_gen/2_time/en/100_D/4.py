def main():
    N, M = list(map(int, input().split()))
    cake = []
    for i in range(N):
        cake.append(list(map(int, input().split())))
    ans = 0
    for i in range(8):
        tmp = []
        for j in range(N):
            tmp.append(sum([cake[j][k] if i&(1<<k) else -cake[j][k] for k in range(3)]))
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)
