def main():
    n = int(input())
    ans = 0
    for i in range(2, 1001):
        for j in range(2, 1001):
            if i ** 3 * j > n:
                break
            ans += 1
    print(ans)
main()
