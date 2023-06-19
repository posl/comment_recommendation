def main():
    N, M, Q = [int(i) for i in input().split()]
    l = []
    for i in range(Q):
        l.append([int(i) for i in input().split()])
    print(l)
    print(N, M, Q)
