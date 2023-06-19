def main():
    n,m = map(int,input().split())
    cnt = [0] * (n+1)
    for i in range(m):
        k = int(input())
        a = list(map(int,input().split()))
        for j in range(k):
            cnt[a[j]] += 1
    for i in range(1,n+1):
        if cnt[i] % 2 != 0:
            print("No")
            return
    print("Yes")
    return
