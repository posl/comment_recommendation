def main():
    n = int(input())
    d = {}
    for i in range(n):
        s,t = input().split()
        t = int(t)
        d[t] = s
    t = sorted(d.keys(),reverse=True)
    print(d[t[1]])
