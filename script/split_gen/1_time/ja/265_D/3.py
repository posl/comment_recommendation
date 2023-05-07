def main():
    n,p,q,r = map(int, input().split())
    a = list(map(int, input().split()))
    ans = "No"
    for i in range(n-3):
        for j in range(i+1,n-2):
            for k in range(j+1,n-1):
                if a[i] * p + a[j] * q + a[k] * r == 0:
                    ans = "Yes"
                    break
    print(ans)
