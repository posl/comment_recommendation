def main():
    D, G = list(map(int, input().split()))
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = list(map(int, input().split()))
    #print(D, G)
    #print(p)
    #print(c)
    #print("")
    min_count = 10000
    for i in range(2**D):
        score = 0
        count = 0
        for j in range(D):
            if i & (1 << j):
                score += (j+1) * 100 * p[j] + c[j]
                count += p[j]
        if score >= G:
            if count < min_count:
                min_count = count
        else:
            for j in range(D-1, -1, -1):
                if not i & (1 << j):
                    for k in range(p[j]-1):
                        score += (j+1) * 100
                        count += 1
                        if score >= G:
                            if count < min_count:
                                min_count = count
                    break
    print(min_count)
