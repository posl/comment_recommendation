def main():
    s = input()
    n = len(s)
    mn = s
    mx = s
    for i in range(n):
        s = s[1:] + s[0]
        mn = min(mn, s)
        mx = max(mx, s)
    print(mn)
    print(mx)
