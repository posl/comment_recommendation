def main():
    N = int(input())
    ans = 0
    while N > 1:
        N = (N + 1) // 2
        ans += 1
    print(ans)
