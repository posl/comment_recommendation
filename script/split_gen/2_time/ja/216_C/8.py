def main():
    N = int(input())
    ans = ''
    while N > 0:
        if N % 2 == 0:
            ans = 'B' + ans
            N = N // 2
        else:
            ans = 'A' + ans
            N = N - 1
    print(ans)
