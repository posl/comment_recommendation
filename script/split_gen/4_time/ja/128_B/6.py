def main():
    N = int(input())
    list = []
    for i in range(N):
        S, P = input().split()
        list.append([S, int(P)])
    list = sorted(list, key=lambda x: (x[0], -x[1]))
    for i in range(N):
        print(list[i][1])
