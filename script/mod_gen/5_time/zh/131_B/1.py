def get_min_diff(N, L):
    #N = len(L)
    L.sort()
    #print L
    if N%2 == 0:
        return sum(L[N/2:]) - sum(L[:N/2])
    else:
        return sum(L[N/2+1:]) - sum(L[:N/2+1])

if __name__ == '__main__':
    get_min_diff()