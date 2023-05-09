def main():
    #input
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    #compute
    ans = 0
    for i in range(k):
        ans += n // a[k-i-1]
        n = n % a[k-i-1]
        if n == 0:
            break
    #output
    print(ans)
