def main():
    N = int(input())
    ans = [0] * (N + 1)
    for i in range(1, N + 1):
        ans[i] = ans[i - 1] + 1
        six = 6
        nine = 9
        while six <= i:
            ans[i] = min(ans[i], ans[i - six] + 1)
            six *= 6
        while nine <= i:
            ans[i] = min(ans[i], ans[i - nine] + 1)
            nine *= 9
    print(ans[N])

if __name__ == '__main__':
    main()