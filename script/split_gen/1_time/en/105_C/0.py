def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = ""
    while N != 0:
        if N % 2 == 0:
            ans += "0"
            N //= -2
        else:
            ans += "1"
            N = N // -2 + 1
    print(ans[::-1])
