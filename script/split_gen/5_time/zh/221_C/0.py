def main():
    N = input()
    n = len(N)
    ans = 0
    for i in range(1, n):
        a = int(N[:i])
        b = int(N[i:])
        ans = max(ans, a * b)
    print(ans)
