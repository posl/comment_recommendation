def main():
    s = input()
    q = int(input())
    tki = [list(map(int, input().split())) for _ in range(q)]
    c = s.count('C')
    for i in range(q):
        t = tki[i][0]
        k = tki[i][1]
        if t % 3 == 0:
            if k <= len(s) - c:
                print(s[k - 1])
            else:
                print(s[k + c - len(s) - 1])
        elif t % 3 == 1:
            if k <= c:
                print(s[len(s) - k])
            else:
                print(s[k - c - 1])
        else:
            if k <= len(s) - c:
                print(s[k + c - 1])
            else:
                print(s[k - len(s) + c - 1])
