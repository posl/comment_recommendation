def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    if k == 1:
        print(0)
        exit()
    ans = 10**9
    for i in range(n-k+1):
        a = x[i]
        b = x[i+k-1]
        ans = min(ans, b-a+min(abs(a), abs(b)))
    print(ans)
