def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = ""
    while N != 0:
        if N % 2 == 0:
            ans = "0" + ans
        else:
            ans = "1" + ans
            N -= 1
        N //= -2
    print(ans)
