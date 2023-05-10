def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    if n%2 == 0:
        b = a[n//2-1]
    else:
        b = a[n//2]
    #print(b)
    ans = 0
    for i in range(n):
        ans += abs(a[i] - (b+i+1))
    print(ans)
