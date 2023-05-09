def f(s, n):
    if len(s) == 0:
        print(n)
        return
    for i in range(len(s)):
        f(s[:i]+s[i+1:], n+s[i])
s = bin(int(input()))[2:]
f(s, 0)

if __name__ == '__main__':
    f()