def main():
    A, B, C, D = map(int, input().split())
    ans = 0
    while A > C * D:
        A += B
        ans += 1
    print(ans if A <= C * D else -1)
