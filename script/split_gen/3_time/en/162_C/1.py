def main():
    K = int(input())
    ans = 0
    for i in range(1, K + 1):
        for j in range(1, K + 1):
            for k in range(1, K + 1):
                ans += gcd(i, j, k)
    print(ans)
