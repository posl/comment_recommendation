def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    #print(a)
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            ans += 1
            if ans == k:
                print(a[i]*a[j])
                exit()
