def main():
    N = int(input())
    S = sum(int(c) for c in str(N))
    print("Yes" if N % S == 0 else "No")
main()
