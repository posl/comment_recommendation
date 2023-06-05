def problem254_d():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        ans += N//i - i
    print(ans*2)
