def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    min_num = 100 * D
    for i in range(2**D):
        total = 0
        num = 0
        for j in range(D):
            if (i >> j) & 1:
                total += 100 * (j + 1) * p[j] + c[j]
                num += p[j]
        if total >= G:
            min_num = min(min_num, num)
        else:
            for j in range(D - 1, -1, -1):
                if not((i >> j) & 1):
                    for k in range(p[j]):
                        total += 100 * (j + 1)
                        num += 1
                        if total >= G:
                            min_num = min(min_num, num)
                            break
                    break
    print(min_num)
