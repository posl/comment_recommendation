def main():
    A, B, X = map(int, input().split())
    if A * 10**9 + B * 10 < X:
        print(10**9)
    else:
        ans = 0
        for i in range(1, 10):
            num = (X - B * i) // A
            if num < 10**i:
                ans = max(ans, num)
        print(ans)
