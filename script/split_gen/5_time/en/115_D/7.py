def main():
    n, x = map(int, input().split())
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        x -= 1
        n -= 1
        ans = 1
        while n > 0:
            if x >= (2**(n+1)-3):
                ans += (2**n)
                x -= (2**(n+1)-3)
            else:
                x -= 1
            n -= 1
        print(ans)
