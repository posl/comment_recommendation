def main():
    N = int(input())
    ans = 0
    i = 2
    while i*i <= N:
        while N%i == 0:
            N //= i
            ans += 1
        i += 1
    if N != 1:
        ans += 1
    print(ans)
main()
