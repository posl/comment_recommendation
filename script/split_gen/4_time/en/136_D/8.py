def main():
    s = input()
    l = len(s)
    ans = [0] * l
    for i in range(1, l):
        if s[i] == "L":
            ans[i - 1] += 1
        else:
            ans[i] += 1
    print(*ans)
