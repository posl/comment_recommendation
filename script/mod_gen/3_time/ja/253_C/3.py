def main():
    import sys
    import bisect
    input = sys.stdin.readline
    Q = int(input())
    query = [list(map(int,input().split())) for _ in range(Q)]
    S = []
    for q in query:
        if q[0] == 1:
            bisect.insort_left(S,q[1])
        elif q[0] == 2:
            for _ in range(min(q[2],S.count(q[1]))):
                S.remove(q[1])
        else:
            print(S[-1]-S[0])

if __name__ == '__main__':
    main()