def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append([int(x) for x in input().split()])
    t = [0] * n
    for i in range(n):
        if s[i][1] == 0:
            t[i] = s[i][0]
        else:
            for j in range(s[i][1]):
                t[i] = max(t[i], t[s[i][2 + j] - 1] + s[i][0])
    print(max(t))
