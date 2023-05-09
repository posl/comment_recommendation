def main():
    n = int(input())
    ans = n-1
    for i in range(2, n):
        j = 2
        while i**j <= n:
            ans -= 1
            j += 1
    print(ans)
