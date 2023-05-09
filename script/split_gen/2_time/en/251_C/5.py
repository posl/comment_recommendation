def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        a, b = input().split()
        s.append(a)
        t.append(int(b))
    best = 0
    best_index = 0
    for i in range(n):
        if s[i] not in s[:i] and best < t[i]:
            best = t[i]
            best_index = i
    print(best_index + 1)
