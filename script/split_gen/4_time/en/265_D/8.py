def main():
    n,p,q,r = map(int, input().split())
    a = list(map(int, input().split()))
    #print(n,p,q,r)
    #print(a)
    a.sort()
    #print(a)
    sum_a = [0]*n
    sum_a[0] = a[0]
    for i in range(1, n):
        sum_a[i] = sum_a[i-1] + a[i]
    #print(sum_a)
    ans = 0
    for i in range(n):
        if (i+3) > n:
            break
        for j in range(i+1, n):
            if (j+2) > n:
                break
            for k in range(j+1, n):
                if (k+1) > n:
                    break
                if (sum_a[i] >= p) and (sum_a[j] >= q) and (sum_a[k] >= r):
                    ans += 1
    print(ans)
