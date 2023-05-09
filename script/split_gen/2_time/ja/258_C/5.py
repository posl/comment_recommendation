def main():
    n, q = map(int, input().split())
    s = input()
    for _ in range(q):
        t, x = input().split()
        x = int(x)
        if t == "1":
            s = s[-x:]+s[:-x]
        else:
            print(s[x-1])
