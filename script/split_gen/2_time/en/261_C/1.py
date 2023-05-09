def main():
    N = int(input())
    S = [input() for _ in range(N)]
    D = {}
    for s in S:
        if s not in D:
            D[s] = 0
            print(s)
        else:
            D[s] += 1
            print(s + '(' + str(D[s]) + ')')
