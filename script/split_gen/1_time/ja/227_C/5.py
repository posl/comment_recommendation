def main():
    N = int(input())
    ans = 0
    for a in range(1, N+1):
        for b in range(a, N+1):
            c = N // (a*b)
            if c >= b:
                ans += c - b + 1
    print(ans)
