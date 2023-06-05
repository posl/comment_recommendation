def main():
    N,K = map(int,input().split())
    h = list(map(int,input().split()))
    cnt = 0
    for i in range(N):
        if h[i] >= K:
            cnt += 1
    print(cnt)
