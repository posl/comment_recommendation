def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [tuple(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2**K):
        bit = bin(i)[2:].zfill(K)
        dish = [0] * (N + 1)
        for j in range(K):
            if bit[j] == '0':
                dish[CD[j][0]] += 1
            else:
                dish[CD[j][1]] += 1
        cnt = 0
        for j in range(M):
            if dish[AB[j][0]] > 0 and dish[AB[j][1]] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
main()
