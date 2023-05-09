def main():
    N = int(input())
    i = 1
    ans = 0
    while i * i <= N:
        ans += N // (i * i)
        i += 1
    print(ans)
