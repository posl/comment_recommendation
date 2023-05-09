def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    #print(p)
    #print(c)
    #print(D, G)
    #print(p)
    #print(c)
    #print("-----")
    min = 1000000
    for i in range(1, 2**D):
        #print("i",i)
        sum = 0
        num = 0
        for j in range(D):
            if (i >> j) & 1:
                sum += 100 * (j + 1) * p[j] + c[j]
                num += p[j]
        #print("sum",sum)
        #print("num",num)
        if sum >= G:
            if num < min:
                min = num
        else:
            for j in range(D):
                if not ((i >> j) & 1):
                    for k in range(p[j]):
                        sum += 100 * (j + 1)
                        num += 1
                        if sum >= G:
                            if num < min:
                                min = num
                            break
                    break
        #print("sum",sum)
        #print("num",num)
        #print("-----")
    print(min)
