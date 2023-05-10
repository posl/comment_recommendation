def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    #print(N, A)
    A.sort()
    #print(N, A)
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            #print(A[i], A[j])
            if A[i] != A[j]:
                cnt += 1
            else:
                break
    print(cnt)
