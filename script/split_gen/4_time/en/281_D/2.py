def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = -1
    for i in range(n-k+1):
        if a[i] % d == 0:
            ans = a[i]
            break
        elif (a[i] + d - 1) // d < (a[i+k-1] + d - 1) // d:
            ans = (a[i] + d - 1) // d * d
            break
    print(ans)
