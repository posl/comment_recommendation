def main():
    s = input()
    n = len(s)
    ans = [0] * n
    i = 0
    while i < n - 1:
        if s[i] == "R":
            j = i
            while j < n - 1 and s[j] == "R":
                j += 1
            if (j - i) % 2 == 0:
                ans[j] += 1
            else:
                ans[j - 1] += 1
        i += 1
    i = n - 1
    while i > 0:
        if s[i] == "L":
            j = i
            while j > 0 and s[j] == "L":
                j -= 1
            if (i - j) % 2 == 0:
                ans[j] += 1
            else:
                ans[j + 1] += 1
        i -= 1
    print(" ".join(map(str, ans)))
