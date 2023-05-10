def main():
    n = int(input())
    s = list(map(int,input().split()))
    t = list(map(int,input().split()))
    ans = [0]*n
    ans[0] = t[0]
    for i in range(1,n):
        ans[i] = min(ans[i-1]+s[i-1],t[i])
    for i in range(n):
        print(ans[i])
