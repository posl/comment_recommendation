def solve():
    s = input()
    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        t %= 3
        k -= 1
        print(s[k] if t == 0 else s[(k + t) % len(s)])
