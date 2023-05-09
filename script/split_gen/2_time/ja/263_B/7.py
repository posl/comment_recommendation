def main():
    n = int(input())
    p = [0] + list(map(int,input().split()))
    ans = 0
    for i in range(1,n+1):
        ans = max(ans,depth(i,p))
    print(ans)
