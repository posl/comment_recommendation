def main():
    N = int(input())
    S = [input() for _ in range(N)]
    D = dict()
    for s in S:
        if s in D:
            D[s] += 1
        else:
            D[s] = 0
        if D[s] == 0:
            print(s)
        else:
            print(s+'('+str(D[s])+')')
