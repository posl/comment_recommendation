def main():
    a, N = map(int, input().split())
    ans = 1
    x = 1
    while x != N:
        x = x * a
        ans += 1
        if x > N:
            ans = -1
            break
    print(ans)
