def lcm(a, b):
    return a * b // gcd(a, b)
N, A, B = map(int, input().split())
ans = (N // A) * (N // B) * lcm(A, B)
ans += (N // A) * (N % B)
ans += (N // B) * (N % A)
ans -= N // lcm(A, B)
print(ans)
