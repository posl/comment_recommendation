def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    ans = []
    for i in range(n-k+1):
        ans.append(sorted(p[i:i+k])[k-1])
    print(*ans,sep="\n")
