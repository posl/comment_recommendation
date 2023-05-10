def main():
    n, m = map(int, input().split())
    p = [0] * n
    s = [0] * n
    for i in range(m):
        ip, is_ = input().split()
        p[int(ip) - 1] += 1
        if is_ == 'AC':
            s[int(ip) - 1] = 1
    print(sum(s), sum([p[i] * s[i] for i in range(n)]))
