def main():
    A, B, C, D = map(int, input().split())
    if B >= C * D:
        print(-1)
        exit()
    ans = 0
    while A > 0:
        if A <= C * D:
            break
        A -= B
        ans += 1
    print(ans)
