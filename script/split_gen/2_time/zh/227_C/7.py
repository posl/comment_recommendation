def main():
    n = int(input())
    ans = 0
    for a in range(1, int(n ** (1 / 3)) + 1):
        for b in range(a, int((n - a ** 3) ** (1 / 2)) + 1):
            c = int((n - a ** 3 - b ** 2) ** (1 / 2))
            if a ** 3 + b ** 2 + c ** 2 + a * b + b * c + c * a == n:
                if a == b == c:
                    ans += 1
                elif a == b or b == c or c == a:
                    ans += 3
                else:
                    ans += 6
    print(ans)
