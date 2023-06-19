def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = []
    c = []
    for i in range(q):
        b_temp, c_temp = map(int, input().split())
        b.append(b_temp)
        c.append(c_temp)
    sum_a = sum(a)
    for i in range(q):
        sum_a += (c[i] - b[i]) * a.count(b[i])
        print(sum_a)
        sum_a -= (c[i] - b[i]) * a.count(b[i])
