def main():
    import sys
    import bisect
    input = sys.stdin.readline
    Q = int(input())
    A = []
    B = []
    C = []
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            bisect.insort(A,query[1])
            bisect.insort(B,query[1])
            bisect.insort(C,query[1])
        elif query[0] == 2:
            if len(A) < query[2]:
                print(-1)
            else:
                print(A[-query[2]])
                bisect.insort(B,A[-query[2]])
                bisect.insort(C,A[-query[2]])
                A.pop(-query[2])
        else:
            if len(B) < query[2]:
                print(-1)
            else:
                print(B[query[2]-1])
                bisect.insort(A,B[query[2]-1])
                bisect.insort(C,B[query[2]-1])
                B.pop(query[2]-1)
    return
