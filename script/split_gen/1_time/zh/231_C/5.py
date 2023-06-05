def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(q):
        x = int(input())
        cnt = 0
        for j in range(n):
            if a[j] >= x:
                cnt += 1
        print(cnt)
