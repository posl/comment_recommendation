def main():
    import sys
    from heapq import heappush, heappop, heapify
    input = sys.stdin.readline
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    S = []
    for i in range(N):
        if A[i][0] == 1:
            heappush(S, A[i][1])
        elif A[i][0] == 2:
            while A[i][2] > 0:
                if S[0] == A[i][1]:
                    heappop(S)
                    A[i][2] -= 1
                else:
                    break
        else:
            print(S[-1] - S[0])
main()

if __name__ == '__main__':
    main()