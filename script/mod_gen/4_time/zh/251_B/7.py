def get_good_int(N,W,A):
    A.sort()
    B = [0]
    for i in range(N):
        for j in range(i,N):
            for k in range(j,N):
                B.append(A[i]+A[j]+A[k])
    B = list(set(B))
    B.sort()
    C = []
    for i in B:
        if i <= W:
            C.append(i)
    return len(C)

if __name__ == '__main__':
    get_good_int()