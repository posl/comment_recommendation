def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    #print(K)
    if A[0] >= 0:
        print(A[K-1])
    elif A[N-1] <= 0:
        if K % 2 == 1:
            print(A[N-K])
        else:
            print(A[N-K+1])
    else:
        l = 0
        r = N-1
        while r-l > 1:
            m = (l+r)//2
            if A[m] < 0:
                l = m
            else:
                r = m
        #print(l)
        #print(r)
        if K <= (l+1)*(N-r):
            l = 0
            r = N-1
            while r-l > 1:
                m = (l+r)//2
                if A[m] < 0:
                    l = m
                else:
                    r = m
            #print(l)
            #print(r)
            if K <= (l+1)*(N-r):
                while True:
                    m = (l+r)//2
                    #print(l)
                    #print(r)
                    #print(m)
                    #print(A[l])
                    #print(A[r])
                    #print(A[m])
                    if A[m]*A[l] > A[m]*A[r]:
                        l = m
                    else:
                        r = m
                    if r-l == 1:
                        break
                #print(l)
                #print(r)
                #print(A[l])
                #print(A[r])
                print(A[l])
            else:
                K = K - (l+1)*(N-r)
                l = 0
                r = N-1
                while r-l > 1:
                    m = (l+r)//2
                    if A[m] < 0:
                        l = m
                    else:
                        r = m
                #print(l)
                #print(r)
                while True:
                    m = (l+r)//2
                    #print(l)
                    #print(r)
                    #print(m)
                    #print(A[l])
                    #print(A[r])
                    #print(A[m])
                    if A[m]*A[l] > A[m]*A[r]:
                        l = m
