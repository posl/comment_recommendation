def triangle_count(L):
    L.sort()
    N = len(L)
    count = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if L[i]+L[j]>L[k]:
                    count += 1
    return count

if __name__ == '__main__':
    triangle_count()