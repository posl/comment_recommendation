def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    lcm = 1
    for a in A:
        lcm = lcm * a // math.gcd(lcm, a)
    ans = M // lcm
    print(ans)
main()
