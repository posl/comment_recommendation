def main():
    n, q = map(int, input().split())
    s = input()
    s = list(s)
    for i in range(q):
        t, x = map(str, input().split())
        x = int(x)
        if t == '1':
            s = s[-x:] + s[:-x]
        if t == '2':
            print(s[x - 1])
