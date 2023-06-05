def main():
    s = input()
    s = s.replace("RL", "R L")
    s = s.split()
    n = len(s)
    ans = [0] * n
    for i in range(n):
        if s[i] == "R":
            ans[i + 1] += ans[i] // 2 + ans[i] % 2
            ans[i] = ans[i] // 2
        else:
            ans[i - 1] += ans[i] // 2
            ans[i] = ans[i] // 2 + ans[i] % 2
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    main()