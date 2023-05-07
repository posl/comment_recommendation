def main():
    from collections import defaultdict
    import sys
    f = sys.stdin
    #f = open("test.txt")
    N = int(f.readline().strip())
    A = [tuple(map(int,f.readline().strip().split())) for i in range(N)]
    D = defaultdict(int)
    S = set()
    for i in range(N):
        if A[i][0] == 1:
            D[A[i][1]] += 1
            S.add(A[i][1])
        elif A[i][0] == 2:
            if D[A[i][1]] > 0:
                D[A[i][1]] -= min(D[A[i][1]],A[i][2])
                if D[A[i][1]] == 0:
                    S.remove(A[i][1])
        else:
            print(max(S)-min(S))
    return
