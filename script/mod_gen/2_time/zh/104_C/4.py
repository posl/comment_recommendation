def main():
    D, G = map(int, input().split())
    PC = [list(map(int, input().split())) for _ in range(D)]
    ans = float('inf')
    for i in range(2**D):
        cnt = 0
        score = 0
        rest_max = -1
        for j in range(D):
            if ((i >> j) & 1):
                score += 100 * (j+1) * PC[j][0] + PC[j][1]
                cnt += PC[j][0]
            else:
                rest_max = j
        if score < G:
            s1 = 100 * (rest_max + 1)
            need = (G - score + s1 - 1) // s1
            if need >= PC[rest_max][0]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()