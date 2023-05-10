def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for i in range(q)]
    ans = []
    for i in range(n-1):
        ans.append(a[i+1]-a[i]-1)
    for i in range(q):
        if k[i] <= a[0]-1:
            print(k[i])
        elif k[i] >= a[n-1]+n-1:
            print(k[i]-(a[n-1]+n-1)+a[n-1])
        else:
            for j in range(n-1):
                if ans[j] >= k[i]:
                    print(a[j]+k[i])
                    break
                else:
                    k[i] -= ans[j]
