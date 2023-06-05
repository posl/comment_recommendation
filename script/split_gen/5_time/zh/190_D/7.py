def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        s = 0
        while s < N:
            s += i
            i += 1
        if s == N:
            ans += 1
    print(ans)
