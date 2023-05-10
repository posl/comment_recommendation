def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n)
    #print(a)
    a = sorted(a)
    #print(a)
    b = a[n//2]
    #print(b)
    ans = 0
    for i in range(n):
        ans += abs(a[i] - b)
    print(ans)
