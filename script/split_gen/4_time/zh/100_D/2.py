def main():
    n,m = map(int,input().split())
    cakes = []
    for _ in range(n):
        cakes.append(list(map(int,input().split())))
    #print(cakes)
    maxVal = 0
    for i in range(1 << n):
        tmp = []
        for j in range(n):
            if i & (1 << j):
                tmp.append(cakes[j])
        if len(tmp) == m:
            #print(tmp)
            val = 0
            for j in range(m):
                val += abs(tmp[j][0])
                val += abs(tmp[j][1])
                val += abs(tmp[j][2])
            if val > maxVal:
                maxVal = val
    print(maxVal)
