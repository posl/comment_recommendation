def main():
    N, M = map(int, input().split())
    cakes = []
    for i in range(N):
        cakes.append(list(map(int, input().split())))
    #print(cakes)
    max = 0
    for i in range(1 << 3):
        #print(i)
        tmp = []
        for j in range(N):
            tmp.append(cakes[j][0] * ((-1) ** ((i >> 0) & 1)) + cakes[j][1] * ((-1) ** ((i >> 1) & 1)) + cakes[j][2] * ((-1) ** ((i >> 2) & 1)))
        tmp.sort(reverse=True)
        #print(tmp)
        sum = 0
        for j in range(M):
            sum += tmp[j]
        if sum > max:
            max = sum
    print(max)
