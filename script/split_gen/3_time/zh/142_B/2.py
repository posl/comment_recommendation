def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    cnt = 0
    for i in range(0,n):
        if h[i] >= k:
            cnt += 1
    print(cnt)
