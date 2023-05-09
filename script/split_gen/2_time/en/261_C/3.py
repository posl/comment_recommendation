def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for s in S:
        if s in d:
            d[s] += 1
            print(s + '(' + str(d[s]) + ')')
        else:
            d[s] = 0
            print(s)
