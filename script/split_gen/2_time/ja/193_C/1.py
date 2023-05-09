def main():
    n = int(input())
    ans = n - 1
    for i in range(2, n):
        for j in range(2, n):
            if i**j <= n:
                ans -= 1
            else:
                break
    print(ans)
