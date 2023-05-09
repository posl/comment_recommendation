def main():
    n = int(input())
    a = [1]
    b = [1]
    c = [1]
    d = [1]
    for i in range(1, 10):
        a.append(6**i)
        b.append(9**i)
        c.append(6**i)
        d.append(9**i)
    for i in range(1, 10):
        for j in range(1, 10):
            c.append(a[i] + b[j])
            d.append(b[i] + a[j])
    c = list(set(c))
    d = list(set(d))
    e = c + d
    e.sort()
    e.reverse()
    count = 0
    for i in e:
        if n >= i:
            count += 1
            n -= i
        if n == 0:
            break
    print(count)
