def main():
    n = int(input())
    a = list(map(int, input().split()))
    gcd = a[0]
    for i in range(1, n):
        gcd = gcd(a[i], gcd)
    print(gcd)
