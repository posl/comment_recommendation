def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    ans = "Yes"
    for i in range(1,N+1):
        if A[i-1] != i:
            ans = "No"
    print(ans)
