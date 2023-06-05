def main():
    n = int(input())
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = i
        j = 6
        while j <= i:
            ans[i] = min(ans[i], ans[i - j] + 1)
            j *= 6
        j = 9
        while j <= i:
            ans[i] = min(ans[i], ans[i - j] + 1)
            j *= 9
    print(ans[n])

if __name__ == '__main__':
    main()