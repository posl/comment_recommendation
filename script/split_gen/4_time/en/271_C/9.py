def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    ans = 0
    for i in range(N-1):
        if a[i+1] <= 2*a[i]:
            ans += 1
        else:
            ans = 0
    print(ans+1)
main()
