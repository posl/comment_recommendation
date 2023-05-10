def main():
    S = input()
    K = int(input())
    T = S.replace('.', ' ')
    T = T.split()
    L = []
    for x in T:
        if len(x) >= K:
            L.append(len(x))
    if len(L) == 0:
        print(0)
    else:
        print(max(L))
