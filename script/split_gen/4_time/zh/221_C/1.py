def main():
    N = input()
    n = len(N)
    ans = 0
    for i in range(1, n):
        A = int(N[:i])
        B = int(N[i:])
        ans = max(ans, A*B)
    print(ans)
main()
