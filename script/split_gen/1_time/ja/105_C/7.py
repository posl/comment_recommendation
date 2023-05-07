def main():
    N = int(input())
    ans = ""
    if N == 0:
        ans = "0"
    while N != 0:
        ans += str(abs(N%(-2)))
        N -= abs(N%(-2))
        N //= (-2)
    print(ans[::-1])
