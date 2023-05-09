def main():
    n, q = map(int, input().split())
    s = input()
    l = [0] * (n + 1)
    for i in range(n):
        l[i + 1] = l[i] + (1 if s[i:i + 2] == 'AC' else 0)
    for _ in range(q):
        a, b = map(int, input().split())
        print(l[b - 1] - l[a - 1])
