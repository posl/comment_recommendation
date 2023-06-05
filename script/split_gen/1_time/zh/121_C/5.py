def main():
    n, m = map(int, input().split())
    #print(n, m)
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        #print(a_i, b_i)
        a.append(a_i)
        b.append(b_i)
    #print(a, b)
    #print(sum(b))
    #print(m)
    if sum(b) <= m:
        print(sum([a[i] * b[i] for i in range(n)]))
    else:
        #print('here')
        total = 0
        for i in range(n):
            if b[i] > m:
                total += a[i] * m
                break
            else:
                total += a[i] * b[i]
                m -= b[i]
        print(total)
