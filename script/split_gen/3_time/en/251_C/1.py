def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(int(t_i))
    best = 0
    best_i = 0
    for i in range(n):
        if s[i] not in s[:i]:
            if t[i] > best:
                best = t[i]
                best_i = i
    print(best_i + 1)
