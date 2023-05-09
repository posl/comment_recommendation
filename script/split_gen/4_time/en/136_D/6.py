def main():
    s = input()
    n = len(s)
    ans = [0] * n
    i = 0
    while i < n:
        if s[i] == "R":
            j = i + 1
            while j < n and s[j] == "R":
                j += 1
            x = j - i
            if x % 2 == 0:
                ans[j - 1] += x // 2
                ans[j] += x // 2
            else:
                ans[j - 1] += x // 2 + 1
                ans[j] += x // 2
            i = j
        else:
            j = i - 1
            while j >= 0 and s[j] == "L":
                j -= 1
            x = i - j
            if x % 2 == 0:
                ans[j] += x // 2
                ans[j + 1] += x // 2
            else:
                ans[j] += x // 2
                ans[j + 1] += x // 2 + 1
            i = j
    print(" ".join(map(str, ans)))
