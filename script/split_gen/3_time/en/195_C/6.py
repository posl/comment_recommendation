def main():
    N = int(input())
    ans = 0
    i = 1
    while i <= N:
        ans += (N - i + 1) * (len(str(i)) - 1)
        i *= 1000
    print(ans)
