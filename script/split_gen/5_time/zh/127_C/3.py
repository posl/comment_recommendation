def main():
    n, m = map(int, input().split())
    l = []
    r = []
    for i in range(m):
        l_, r_ = map(int, input().split())
        l.append(l_)
        r.append(r_)
    l.sort()
    r.sort()
    if l[-1] > r[0]:
        print(0)
    else:
        print(r[0] - l[-1] + 1)
