def main():
    import bisect
    Q = int(input())
    S = []
    for _ in range(Q):
        query = input().split()
        if query[0] == '1':
            bisect.insort(S, int(query[1]))
        elif query[0] == '2':
            x, c = int(query[1]), int(query[2])
            for _ in range(min(c, S.count(x))):
                S.remove(x)
        else:
            print(S[-1] - S[0])
