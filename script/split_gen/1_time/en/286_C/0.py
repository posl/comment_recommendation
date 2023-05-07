def main():
    n, a, b = map(int, input().split())
    s = input()
    c = 0
    d = 0
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            c += 1
    if c == 0:
        print(0)
    elif c == 1:
        print(a)
    else:
        print(a*(c-1)+b)
