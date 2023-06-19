def main():
    s = input()
    q = int(input())
    tks = []
    for i in range(q):
        tks.append(tuple(map(int, input().split())))
    for t, k in tks:
        t = t % 3
        if t == 0:
            print(s[k-1])
        elif t == 1:
            print(s[k-1].translate(str.maketrans('abc', 'bca')))
        else:
            print(s[k-1].translate(str.maketrans('abc', 'cab')))
