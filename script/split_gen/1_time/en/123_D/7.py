def main():
    # Get input here
    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    # Compute desired result here
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)
    # Print result here
    ans = []
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if (i+1)*(j+1)*(k+1) <= k:
                    break
                ans.append(a[i] + b[j] + c[k])
    ans.sort(reverse=True)
    for i in range(k):
        print(ans[i])
