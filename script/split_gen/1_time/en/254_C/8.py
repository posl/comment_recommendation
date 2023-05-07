def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    #print(N,K,A)
    #print(1<=N<=2*10**5)
    #print(1<=K<=N-1)
    #print(1<=A[i]<=10**9)
    #print(all(1<=A[i]<=10**9 for i in range(N)))
    A_sorted = sorted(A)
    if A_sorted == A:
        print("Yes")
        return
    if K == 1:
        print("No")
        return
    if N%K == 0:
        print("Yes")
        return
    if N%K == 1:
        print("No")
        return
    if N%K == 2:
        if A_sorted[0] == A_sorted[1] and A_sorted[-1] == A_sorted[-2]:
            print("Yes")
            return
        else:
            print("No")
            return
    if N%K == 3:
        if A_sorted[0] == A_sorted[1] and A_sorted[-1] == A_sorted[-2]:
            print("Yes")
            return
        if A_sorted[0] == A_sorted[1] and A_sorted[1] == A_sorted[2]:
            print("Yes")
            return
        if A_sorted[-1] == A_sorted[-2] and A_sorted[-2] == A_sorted[-3]:
            print("Yes")
            return
        print("No")
        return
    if N%K == 4:
        if A_sorted[0] == A_sorted[1] and A_sorted[1] == A_sorted[2] and A_sorted[-1] == A_sorted[-2]:
            print("Yes")
            return
        if A_sorted[0] == A_sorted[1] and A_sorted[1] == A_sorted[2] and A_sorted[2] == A_sorted[3]:
            print("Yes")
            return
        if A_sorted[-1] == A_sorted[-2] and A_sorted[-2] == A_sorted[-3] and A_sorted[-3] == A_sorted[-4]:
            print("Yes")
            return
        if A_sorted[0] == A_sorted[1] and A_sorted[-1] == A_sorted[-2] and A_sorted[-
