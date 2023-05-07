def main():
    N = int(input())
    A = list(map(int,input().split()))
    #print(N)
    #print(A)
    #A = [0] + A
    #print(A)
    cnt = 0
    for i in range(1,N+1):
        if A[i-1] == i:
            if i == N:
                cnt += 1
            elif A[i] == i + 1:
                cnt += 1
        #print(i,cnt)
    print(cnt)
