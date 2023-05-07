def main():
    N = input()
    N = N.zfill(10)
    print("Yes" if N == N[::-1] else "No")
