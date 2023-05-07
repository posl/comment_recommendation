def main():
    N,M = map(int,input().split())
    ans = "No"
    for i in range(M):
        k,*x = map(int,input().split())
        for j in range(1,k):
            if x[j-1]+1 == x[j]:
                ans = "Yes"
    print(ans)
