def main():
    N, Q = map(int, input().split())
    S = input()
    l = []
    r = []
    for _ in range(Q):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)
    print(N, Q)
    print(S)
    print(l)
    print(r)
