def main():
    n = int(input())
    s = [tuple(map(int, input().split())) for _ in range(n)]
    t = [tuple(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s[i], t[j] = t[j], s[i]
            if set(s) == set(t):
                print('Yes')
                return
            s[i], t[j] = t[j], s[i]
    print('No')
