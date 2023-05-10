def main():
    n, q = map(int, input().split())
    s = input()
    s = list(s)
    for i in range(q):
        t, x = map(int, input().split())
        if t == 1:
            s = s[-x:] + s[:-x]
        else:
            print(s[x - 1])
