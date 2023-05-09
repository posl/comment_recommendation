def main():
    n = int(input())
    s = []
    t = []
    for _ in range(n):
        a, b = input().split()
        s.append(a)
        t.append(int(b))
    ans = 0
    max_t = 0
    for i in range(n):
        if s[i] not in s[:i] and t[i] > max_t:
            ans = i + 1
            max_t = t[i]
    print(ans)
