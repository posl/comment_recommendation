def main():
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    t = [list(map(int, input().split())) for _ in range(n)]
    s.sort()
    t.sort()
    s = [[s[i][0] - t[0][0], s[i][1] - t[0][1]] for i in range(n)]
    t = [[t[i][0] - t[0][0], t[i][1] - t[0][1]] for i in range(n)]
    for i in range(n):
        if s[i] != t[i]:
            print('No')
            exit()
    print('Yes')
