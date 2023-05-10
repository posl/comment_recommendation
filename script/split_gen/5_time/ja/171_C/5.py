def main():
    N = int(input())
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    ans = ''
    while N > 0:
        N -= 1
        ans = alpha[N % 26] + ans
        N //= 26
    print(ans)
