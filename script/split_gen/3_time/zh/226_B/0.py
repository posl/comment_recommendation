def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    print(len(set(tuple(l) for l in L)))
