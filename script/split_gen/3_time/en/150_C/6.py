def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    P = [i - 1 for i in P]
    Q = [i - 1 for i in Q]
    P = [i for i in range(N)]
    Q = [i for i in range(N)]
    print(P)
    print(Q)
    ans = abs(P - Q)
    print(ans)
