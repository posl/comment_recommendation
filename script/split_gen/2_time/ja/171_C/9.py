def main():
    # N = int(input())
    N = 123456789
    # N = 2
    ans = ''
    while N > 0:
        N -= 1
        ans = chr(ord('a') + N % 26) + ans
        N //= 26
    print(ans)
