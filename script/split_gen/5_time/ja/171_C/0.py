def main():
    N = int(input())
    ans = ""
    while N > 0:
        if N % 26 == 0:
            ans = "z" + ans
            N -= 26
        else:
            ans = chr(96 + N % 26) + ans
        N = int(N / 26)
    print(ans)
