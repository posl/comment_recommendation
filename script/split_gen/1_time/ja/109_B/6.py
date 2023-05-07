def main():
    N = int(input())
    W = [input() for i in range(N)]
    d = {}
    for w in W:
        if w in d:
            print("No")
            return
        d[w] = True
        if len(w) == 1:
            continue
        if w[:-1] not in d:
            print("No")
            return
    print("Yes")
