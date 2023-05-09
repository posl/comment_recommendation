def main():
    N = int(input())
    ans = 0
    i = 1
    while i < N:
        i *= 2
        ans += 1
    print(ans)
