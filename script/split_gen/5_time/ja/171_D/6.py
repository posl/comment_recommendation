def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = [0]*q
    c = [0]*q
    for i in range(q):
        b[i], c[i] = map(int, input().split())
    #print(n, a, q, b, c)
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    #print(d)
    s = sum(a)
    for i in range(q):
        if b[i] in d:
            s = s - b[i]*d[b[i]] + c[i]*d[b[i]]
            if c[i] in d:
                d[c[i]] += d[b[i]]
            else:
                d[c[i]] = d[b[i]]
            d[b[i]] = 0
        print(s)
