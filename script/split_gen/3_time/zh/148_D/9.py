def main():
    n = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    for i in range(n):
        if a[i] == i+1:
            cnt += 1
    if cnt == n:
        print(0)
    elif cnt >= n-1:
        print(n-cnt)
    else:
        print(-1)
main()
