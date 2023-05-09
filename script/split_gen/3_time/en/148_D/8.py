def main():
    N = int(input())
    a = list(map(int, input().split()))
    #print(N)
    #print(a)
    ans = 0
    #print(max(a))
    if N == 1:
        if a[0] == 1:
            print(0)
        else:
            print(-1)
        return
    if max(a) < N:
        print(-1)
        return
    if min(a) > 1:
        print(-1)
        return
    for i in range(1, N):
        if a[i] == a[i-1] + 1:
            continue
        elif a[i] == a[i-1]:
            ans += 1
        else:
            print(-1)
            return
    print(ans)
main()
