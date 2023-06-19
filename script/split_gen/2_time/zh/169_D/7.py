def main():
    n = int(input())
    ans = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            m = n
            while m % i == 0:
                m //= i
            if m % i == 1:
                m = n
                while m % i == 0:
                    m //= i
                ans += 1
    m = n - 1
    for i in range(2, int(m ** 0.5) + 1):
        if m % i == 0:
            ans += 1
            while m % i == 0:
                m //= i
    if m != 1:
        ans += 1
    print(ans)
