def main():
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    t = [list(map(int, input().split())) for _ in range(n)]
    s.sort(key=lambda x: x[0]**2+x[1]**2)
    t.sort(key=lambda x: x[0]**2+x[1]**2)
    for i in range(n):
        if s[i][0] != t[i][0] or s[i][1] != t[i][1]:
            print('No')
            return
    print('Yes')
