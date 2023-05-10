def main():
    n = int(input())
    ans = 0
    for i in range(1, n):
        for j in range(1, n):
            if i * j < n:
                ans += 1
            else:
                break
    print(ans)
