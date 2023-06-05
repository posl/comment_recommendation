def main():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    min_num = 10000
    for i in range(2**D):
        num = 0
        score = 0
        rest_max = -1
        for j in range(D):
            if ((i >> j) & 1):
                score += 100 * (j+1) * pc[j][0] + pc[j][1]
                num += pc[j][0]
            else:
                rest_max = j
        if score < G:
            s1 = 100 * (rest_max + 1)
            need = (G - score + s1 - 1) // s1
            if need >= pc[rest_max][0]:
                continue
            num += need
        min_num = min(min_num, num)
    print(min_num)
