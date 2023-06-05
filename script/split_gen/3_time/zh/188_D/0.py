def main():
    n,c = map(int,input().split())
    a = []
    b = []
    d = []
    for i in range(n):
        a1,b1,d1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
        d.append(d1)
    total = 0
    for i in range(n):
        total += d[i]
    print(total)
    return total
