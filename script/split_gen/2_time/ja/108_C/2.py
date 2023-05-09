def main():
    n,k = map(int,input().split())
    a = [0] * k
    b = [0] * k
    c = [0] * k
    for i in range(1,n+1):
        a[i%k] += 1
        b[i%k] += 1
        c[i%k] += 1
    ans = 0
    for i in range(k):
        for j in range(k):
            for l in range(k):
                if (i+j+l)%k == 0:
                    ans += a[i]*b[j]*c[l]
    print(ans)
