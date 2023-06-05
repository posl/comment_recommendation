def getRank(p):
    n = len(p)
    rank = 0
    for i in range(n):
        for j in range(i+1,n):
            if p[i] > p[j]:
                rank += 1
    return rank

if __name__ == '__main__':
    getRank()