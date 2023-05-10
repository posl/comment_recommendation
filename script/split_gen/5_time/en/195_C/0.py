def main():
    n = int(input())
    ans = 0
    i = 3
    while i <= len(str(n)):
        ans += n - 10**(i-1) + 1
        i += 3
    print(ans)
    return 0
