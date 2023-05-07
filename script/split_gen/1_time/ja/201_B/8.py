def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(input().split())
    for i in range(n):
        t.append(int(s[i][1]))
    t.sort(reverse=True)
    print(s[t.index(t[1])][0])
