def takoyaki_festival(N, d):
    sum = 0
    for i in range(N):
        for j in range(i+1,N):
            sum += d[i]*d[j]
    return sum

if __name__ == '__main__':
    takoyaki_festival()