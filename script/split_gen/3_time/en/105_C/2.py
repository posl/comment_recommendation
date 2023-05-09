def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = ""
    while N != 0:
        if N % 2 == 0:
            ans = "0" + ans
            N = N // -2
        else:
            ans = "1" + ans
            N = (N - 1) // -2
    print(ans)
