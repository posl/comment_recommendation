def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for s in S:
        d[s] = d.get(s, 0) + 1
        if d[s] == 1:
            print(s)
        else:
            print(s + "(" + str(d[s] - 1) + ")")
