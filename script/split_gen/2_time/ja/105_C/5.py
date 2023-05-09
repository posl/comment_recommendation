def main():
    N = int(input())
    if N == 0:
        print(0)
    else:
        ans = ""
        while N != 0:
            ans = str(N % -2) + ans
            N = (N - (N % -2)) // -2
        print(ans)
