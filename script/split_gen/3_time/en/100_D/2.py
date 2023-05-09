def main():
    N, M = map(int, input().split())
    cake = []
    for i in range(N):
        cake.append(list(map(int, input().split())))
    ans = 0
    for i in range(8):
        cake.sort(key=lambda x: x[0] if i & 1 == 0 else -x[0])
        cake.sort(key=lambda x: x[1] if i & 2 == 0 else -x[1])
        cake.sort(key=lambda x: x[2] if i & 4 == 0 else -x[2])
        ans = max(ans, sum(cake[j][0] + cake[j][1] + cake[j][2] for j in range(M)))
    print(ans)
