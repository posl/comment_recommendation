def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    ans = 0
    ans += a + (10 - a % 10) % 10
    ans += b + (10 - b % 10) % 10
    ans += c + (10 - c % 10) % 10
    ans += d + (10 - d % 10) % 10
    ans += e + (10 - e % 10) % 10
    ans -= max(a, b, c, d, e) + (10 - max(a, b, c, d, e) % 10) % 10
    print(ans)
