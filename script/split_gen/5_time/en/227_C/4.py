def main():
    N = int(input())
    ans = 0
    for a in range(1,N+1):
        ans += (N // a) * (N // a + 1) // 2 * a
    print(ans)
