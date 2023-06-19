def main():
    n,x,y = map(int,input().split())
    for k in range(1,n):
        ans = 0
        for i in range(1,n):
            for j in range(i+1,n+1):
                if i == x and j == y:
                    continue
                d = min(j-i,abs(x-i)+1+abs(y-j))
                if d == k:
                    ans += 1
        print(ans)
