def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = []
    c = []
    for i in range(q):
        b1, c1 = map(int, input().split())
        b.append(b1)
        c.append(c1)
    a_sum = sum(a)
    b_sum = {}
    for i in range(n):
        if a[i] in b_sum:
            b_sum[a[i]] += 1
        else:
            b_sum[a[i]] = 1
    for i in range(q):
        if b[i] in b_sum:
            a_sum += (c[i] - b[i]) * b_sum[b[i]]
            if c[i] in b_sum:
                b_sum[c[i]] += b_sum[b[i]]
            else:
                b_sum[c[i]] = b_sum[b[i]]
            b_sum[b[i]] = 0
        print(a_sum)
