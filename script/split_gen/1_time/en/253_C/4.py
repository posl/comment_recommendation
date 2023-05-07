def main():
    import sys
    input = sys.stdin.readline
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    S = []
    for q in query:
        if q[0] == 1:
            S.append(q[1])
        elif q[0] == 2:
            if q[2] >= S.count(q[1]):
                S = [s for s in S if s != q[1]]
            else:
                for _ in range(q[2]):
                    S.remove(q[1])
        else:
            print(max(S) - min(S))
    return
