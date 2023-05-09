def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, X)
    #print(A)
    l = [0] * N
    l[X-1] = 1
    #print(l)
    i = X-1
    while 1:
        #print(i, A[i])
        i = A[i] - 1
        l[i] += 1
        if l[i] == 2:
            break
    print(sum(l))
