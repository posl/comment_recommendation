def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        c, d = map(int, input().split())
        a.append(c)
        b.append(d)
    print(min(max(a), max(b)))
