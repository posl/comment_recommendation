def solve():
    N,x,y = map(int,input().split())
    A = list(map(int,input().split()))
    A.append(0)
    A.insert(0,0)
    ans = "No"
    for i in range(1,N+1):
        for j in range(i+1,N+2):
            if A[i] > A[j]:
                A[i],A[j] = A[j],A[i]
        for j in range(1,N+1):
            if A[j] > A[j+1]:
                break
            if j == N:
                ans = "Yes"
                break
    if ans == "Yes":
        if A[1] == 0 and A[2] == 0:
            ans = "No"
        if A[1] == 0 and A[2] == 1:
            ans = "No"
        if A[1] == 0 and A[2] == 2 and A[3] == 2:
            ans = "No"
        if A[1] == 0 and A[2] == 3 and A[3] == 3:
            ans = "No"
        if A[1] == 0 and A[2] == 4 and A[3] == 4:
            ans = "No"
        if A[1] == 0 and A[2] == 5 and A[3] == 5:
            ans = "No"
        if A[1] == 0 and A[2] == 6 and A[3] == 6:
            ans = "No"
        if A[1] == 0 and A[2] == 7 and A[3] == 7:
            ans = "No"
        if A[1] == 0 and A[2] == 8 and A[3] == 8:
            ans = "No"
        if A[1] == 0 and A[2] == 9 and A[3] == 9:
            ans = "No"
        if A[1] == 0 and A[2] == 10 and A[3] == 10:
            ans = "No"
        if A[1] == 0 and A[2] == 1 and A[3] == 1 and A[
