def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    for i in range(n):
        if s[i] in t:
            print('Yes')
        else:
            print('No')
