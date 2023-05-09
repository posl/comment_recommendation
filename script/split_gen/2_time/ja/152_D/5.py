def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i < 10:
            ans += 1
        else:
            if i % 10 == (i // 10) % 10:
                ans += 1
    print(ans)
