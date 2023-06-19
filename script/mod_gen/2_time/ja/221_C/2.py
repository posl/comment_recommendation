def main():
    N = input()
    N_len = len(N)
    ans = 0
    for i in range(1, N_len):
        A = int(N[:i])
        B = int(N[i:])
        ans = max(ans, A*B)
    print(ans)
main()
