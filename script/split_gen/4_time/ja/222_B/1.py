def main():
    N, P = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if a[i] < P:
            cnt += 1
    print(cnt)
main()
