def main():
    N = int(input())
    a = list(map(int, input().split()))
    if a[0] != 1:
        print(-1)
        return
    count = 0
    for i in range(1, N):
        if a[i] - a[i-1] > 1:
            print(-1)
            return
        elif a[i] - a[i-1] == 1:
            count += 1
    print(N - 1 - count)
main()
