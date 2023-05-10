def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(n-k+1):
        right = x[i+k-1]
        left = x[i]
        ans = min(ans, right-left+min(abs(left), abs(right)))
    print(ans)
