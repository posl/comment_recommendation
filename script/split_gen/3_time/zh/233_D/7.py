def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, A)
    sum = 0
    for i in range(N):
        sum += A[i]
    #print(sum)
    if sum < K:
        print(0)
        return
    else:
        pass
    #print(A)
    #print(len(A))
    for i in range(N):
        if A[i] == K:
            print(1)
            return
        else:
            pass
    #print("OK")
    for i in range(N):
        if A[i] > K:
            A[i] = 0
        else:
            pass
    #print(A)
    for i in range(N):
        if A[i] == 0:
            A[i] = 1
        else:
            pass
    #print(A)
    for i in range(N):
        if i == 0:
            pass
        else:
            A[i] += A[i-1]
    #print(A)
    for i in range(N):
        if A[i] == K:
            print(1)
            return
        else:
            pass
    #print("OK")
    for i in range(N):
        if A[i] < K:
            A[i] = 0
        else:
            pass
    #print(A)
    for i in range(N):
        if A[i] == 0:
            A[i] = 1
        else:
            pass
    #print(A)
    for i in range(N):
        if i == 0:
            pass
        else:
            A[i] += A[i-1]
    #print(A)
    for i in range(N):
        if A[i] == K:
            print(1)
            return
        else:
            pass
    #print("OK")
    for i in range(N):
        if A[i] > K:
            A[i] = 0
        else:
            pass
    #print(A)
    for i in range(N):
        if A[i] == 0:
            A[i] = 1
        else:
            pass
    #print(A)
    for i in range(N):
        if i == 0:
            pass
        else:
            A[i] += A[i-1
