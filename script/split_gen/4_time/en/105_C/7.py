def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    ans = ''
    while n != 0:
        r = n % 2
        n = n // (-2)
        if r == -1:
            r = 1
            n += 1
        ans = str(r) + ans
    print(ans)
