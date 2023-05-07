def main():
    n, m = map(int, input().split())
    p = [0] * m
    s = [0] * m
    for i in range(m):
        p[i], s[i] = input().split()
        p[i] = int(p[i])
        if s[i] == "AC":
            s[i] = 1
        else:
            s[i] = 0
    wa = [0] * (n + 1)
    ac = [0] * (n + 1)
    for i in range(m):
        if ac[p[i]] == 0:
            if s[i] == 1:
                ac[p[i]] = 1
            else:
                wa[p[i]] += 1
    correct = 0
    penalty = 0
    for i in range(1, n + 1):
        if ac[i] == 1:
            correct += 1
            penalty += wa[i]
    print(correct, penalty)
