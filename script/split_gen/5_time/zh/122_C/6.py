def main():
    n, q = map(int, input().split())
    s = input()
    t = [0]
    for i in range(1, n):
        t.append(t[i-1])
        if s[i-1] == 'A' and s[i] == 'C':
            t[i] += 1
    for _ in range(q):
        l, r = map(int, input().split())
        print(t[r-1]-t[l-1])
