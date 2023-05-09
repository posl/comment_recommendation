def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(N):
        flag = 1
        for j in range(M):
            if AB[j][0] == i + 1:
                if H[i] <= H[AB[j][1] - 1]:
                    flag = 0
                    break
            if AB[j][1] == i + 1:
                if H[i] <= H[AB[j][0] - 1]:
                    flag = 0
                    break
        if flag == 1:
            ans += 1
    print(ans)
