def main():
    n, q = map(int, input().split())
    s = input()
    l = [0] * (n + 1)
    for i in range(n - 1):
        if s[i] == "A" and s[i + 1] == "C":
            l[i + 1] = l[i] + 1
        else:
            l[i + 1] = l[i]
    for _ in range(q):
        a, b = map(int, input().split())
        print(l[b - 1] - l[a - 1])
