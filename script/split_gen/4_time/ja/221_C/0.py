def main():
    N = input()
    ans = 0
    for i in range(1, len(N)):
        a = int(N[:i])
        b = int(N[i:])
        ans = max(ans, a * b)
    print(ans)
main()
