def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    if A[0] != 0:
        print(0)
    else:
        ans = 0
        for i in range(1,N):
            if A[i] - A[i-1] > 1:
                ans = A[i-1] + 1
                break
        print(ans)
