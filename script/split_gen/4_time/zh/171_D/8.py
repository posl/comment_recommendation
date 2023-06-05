def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = []
    c = []
    for _ in range(q):
        b_, c_ = map(int, input().split())
        b.append(b_)
        c.append(c_)
    sum_a = sum(a)
    for i in range(q):
        sum_a = sum_a + (c[i] - b[i]) * a.count(b[i])
        print(sum_a)
