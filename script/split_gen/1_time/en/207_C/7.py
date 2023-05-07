def main():
    N = int(input())
    A = []
    for i in range(N):
        t,l,r = map(int,input().split())
        A.append([t,l,r])
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if A[i][0] == 1 and A[j][0] == 1:
                if A[i][1] <= A[j][1] <= A[i][2] or A[j][1] <= A[i][1] <= A[j][2]:
                    ans += 1
            elif A[i][0] == 2 and A[j][0] == 2:
                if A[i][1] < A[j][1] < A[i][2] or A[j][1] < A[i][1] < A[j][2]:
                    ans += 1
            elif A[i][0] == 3 and A[j][0] == 3:
                if A[i][1] < A[j][1] <= A[i][2] or A[j][1] < A[i][1] <= A[j][2]:
                    ans += 1
            elif A[i][0] == 4 and A[j][0] == 4:
                if A[i][1] < A[j][1] < A[i][2] or A[j][1] < A[i][1] < A[j][2]:
                    ans += 1
            elif A[i][0] == 1 and A[j][0] == 2:
                if A[i][1] <= A[j][1] < A[i][2]:
                    ans += 1
            elif A[i][0] == 2 and A[j][0] == 1:
                if A[j][1] <= A[i][1] < A[j][2]:
                    ans += 1
            elif A[i][0] == 1 and A[j][0] == 3:
                if A[i][1] <= A[j][1] <= A[i][2]:
                    ans += 1
            elif A[i][0] == 3 and A[j][0] == 1:
                if A[j][1] <= A[i][1] <= A[j][2]:
                    ans += 1
            elif A[i][0]
