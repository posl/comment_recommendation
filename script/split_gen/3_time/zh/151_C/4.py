def main():
    n, m = map(int, input().split())
    ac = [0] * n
    wa = [0] * n
    for i in range(m):
        p, s = input().split()
        p = int(p) - 1
        if s == "AC":
            ac[p] = 1
        else:
            if ac[p] == 0:
                wa[p] += 1
    print(sum(ac), sum([ac[i] * wa[i] for i in range(n)]))
