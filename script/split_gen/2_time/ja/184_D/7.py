def main():
    A, B, C = map(int, input().split())
    ans = 0
    for i in range(100):
        ans += i * (A + B + C) * (A + B + C - 1) / (100 - i) / 100
        A, B, C = B, C, A
    print(ans)
