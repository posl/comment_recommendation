def main():
    N = int(input())
    ans = 0
    while N > 1:
        N -= 1
        ans += 1
        N //= 2
    print(ans)
