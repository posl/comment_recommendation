def main():
    N = int(input())
    ans = 0
    for a in range(1, N+1):
        for b in range(1, N//a+1):
            c = N//a//b
            if a <= b <= c:
                ans += 1
    print(ans)
