def main():
    n, m = map(int, input().split())
    l = [0] * (n + 1)
    for i in range(m):
        l_i, r_i = map(int, input().split())
        l[l_i - 1] += 1
        l[r_i] -= 1
    for i in range(1, n + 1):
        l[i] += l[i - 1]
    print(l.count(m))
