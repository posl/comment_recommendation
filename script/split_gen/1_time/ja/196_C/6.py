def main():
    N = int(input())
    ans = 0
    for i in range(1, 11):
        if N >= 10 ** i:
            ans += 9 * 10 ** ((i - 1) // 2)
        else:
            ans += (N - 10 ** (i - 1) + 1) // 2
            break
    print(ans)
