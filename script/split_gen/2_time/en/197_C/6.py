def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = [0]*30
    for i in range(n):
        for j in range(30):
            if a[i]&(1<<j):
                b[j]+=1
    ans = 0
    for i in range(30):
        if b[i]%2==1:
            ans += (1<<i)
    print(ans)
