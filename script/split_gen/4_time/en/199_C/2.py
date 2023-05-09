def main():
    n = int(input())
    s = input()
    q = int(input())
    s = list(s)
    for i in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            s[a-1], s[b-1] = s[b-1], s[a-1]
        else:
            s[:n], s[n:] = s[n:], s[:n]
    print(''.join(s))
