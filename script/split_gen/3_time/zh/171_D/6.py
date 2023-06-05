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
    for i in range(q):
        a_sum += (c[i]-b[i])*a.count(b[i])
        print(a_sum)
        a = [c[i] if a_i == b[i] else a_i for a_i in a]
