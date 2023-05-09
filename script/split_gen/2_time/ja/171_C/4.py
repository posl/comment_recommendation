def main():
    n = int(input())
    n -= 1
    ans = ""
    while n >= 0:
        ans = chr((n % 26) + ord('a')) + ans
        n = n // 26 - 1
    print(ans)
