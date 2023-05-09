def main():
    n = input()
    n = int(n)
    ans = 0
    for i in range(1,len(str(n))):
        ans += i * (n // (10 ** i) - n // (10 ** (i + 1)) * 10)
    print(ans)
