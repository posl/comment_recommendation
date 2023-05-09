def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A = A[::-1]
    #print(A)
    #print(A[0])
    for i in range(A[0],1,-1):
        #print(i)
        cnt = 0
        for j in range(N):
            if A[j] % i == 0:
                cnt += 1
        if cnt >= 2:
            print(i)
            return
    print(1)
