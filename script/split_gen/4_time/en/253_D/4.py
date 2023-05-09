def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N, A, B = map(int, input().split())
g = gcd(A, B)
lcm = A * B // g
ans = N - (N // A + N // B - N // lcm)
print(ans)
