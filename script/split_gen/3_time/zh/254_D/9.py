def main():
    n = int(input())
    i = 1
    ans = 0
    while i*i <= n:
        j = 1
        while i*j <= n:
            ans += 1
            j += 1
        i += 1
    print(ans)
