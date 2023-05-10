def main():
    N = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if a[i] != i+1:
            cnt += 1
    if cnt > 2:
        print(-1)
    else:
        print(cnt)
