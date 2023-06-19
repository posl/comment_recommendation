def main():
    N, M = map(int, input().split())
    A = []
    for _ in range(M):
        A.append(list(map(int, input().split()))[1:])
    from collections import Counter
    C = Counter()
    for a in A:
        C.update(a)
    for v in C.values():
        if v % 2 == 1:
            print('No')
            return
    print('Yes')
