def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = []
    c = []
    for i in range(q):
        b_i, c_i = map(int, input().split())
        b.append(b_i)
        c.append(c_i)
    a_sum = sum(a)
    b_sum = dict(zip(range(1, n+1), a))
    for i in range(q):
        a_sum += (c[i] - b[i]) * b_sum[b[i]]
        print(a_sum)
        b_sum[c[i]] = b_sum.get(c[i], 0) + b_sum[b[i]]
        b_sum[b[i]] = 0

if __name__ == '__main__':
    main()