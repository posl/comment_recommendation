def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    s = sum(a)**2
    t = sum([i**2 for i in a])
    print((s-t)//2%mod)
main()
