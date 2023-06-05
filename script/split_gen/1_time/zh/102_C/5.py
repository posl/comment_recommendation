def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = 0
    for i in range(n):
        b += a[i] - i - 1
    b = b // n
    c = [b-1,b,b+1]
    ans = float('inf')
    for i in c:
        tmp = 0
        for j in range(n):
            tmp += abs(a[j] - (i+j+1))
        ans = min(ans,tmp)
    print(ans)
