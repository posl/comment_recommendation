def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                ans += 0
            else:
                ans += i
        else:
            if i % 5 == 0:
                ans += i
            else:
                ans += i
    print(ans)
