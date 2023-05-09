def main():
    N, M = map(int, input().split())
    AB = []
    for _ in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0])
    ans = 0
    i = 0
    for _ in range(M):
        while i < N and AB[i][0] <= _ + 1:
            AB[i][0] = 0
            i += 1
        if i == N:
            break
        ans += AB[i][1]
        AB[i][0] -= _ + 1
    print(ans)
main()
