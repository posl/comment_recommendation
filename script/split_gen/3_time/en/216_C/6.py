def main():
    N = int(input())
    ans = ''
    while N > 0:
        if N % 2 == 1:
            ans += 'A'
            N -= 1
        else:
            ans += 'B'
            N //= 2
    ans = ans[::-1]
    print(ans)
