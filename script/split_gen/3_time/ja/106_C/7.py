def main():
    s = input()
    k = int(input())
    def f(s):
        t = ""
        for c in s:
            if c != "1":
                t += c * int(c)
            else:
                t += c
        return t
    for _ in range(k):
        s = f(s)
    print(s[k - 1])
