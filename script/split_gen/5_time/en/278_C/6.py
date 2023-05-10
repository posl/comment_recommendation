def main():
    N, Q = map(int, input().split())
    follow = [[False for _ in range(N)] for _ in range(N)]
    for _ in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            follow[A - 1][B - 1] = True
        elif T == 2:
            follow[A - 1][B - 1] = False
        else:
            if follow[A - 1][B - 1]:
                print('Yes')
            else:
                print('No')
