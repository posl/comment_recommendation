def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2 ** K):
        dish = [0] * (N + 1)
        for j in range(K):
            if ((i >> j) & 1) == 0:
                dish[CD[j][0]] = 1
            else:
                dish[CD[j][1]] = 1
        tmp = 0
        for a, b in AB:
            if dish[a] == 1 and dish[b] == 1:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)
