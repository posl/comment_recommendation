def main():
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] != 1:
        print(-1)
        return
    cnt = 0
    for i in range(n-1):
        if a[i+1] - a[i] == 1:
            cnt += 1
        elif a[i+1] == a[i]:
            cnt += 1
        elif a[i+1] - a[i] > 1:
            print(-1)
            return
    print(n - cnt - 1)
main()
