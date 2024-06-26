def solve():
    D, G = map(int, input().split())
    PC = [list(map(int, input().split())) for _ in range(D)]
    ans = float('inf')
    for i in range(1 << D):
        score = 0
        count = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                score += 100 * (j + 1) * PC[j][0] + PC[j][1]
                count += PC[j][0]
            else:
                rest_max = j
        if score < G:
            s1 = 100 * (rest_max + 1)
            need = (G - score + s1 - 1) // s1
            if need >= PC[rest_max][0]:
                continue
            count += need
        ans = min(ans, count)
    print(ans)

if __name__ == '__main__':
    solve()