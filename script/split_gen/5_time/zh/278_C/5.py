def main():
    N, Q = map(int, input().split())
    follow = [[0 for i in range(N)] for j in range(N)]
    for i in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a-1][b-1] = 1
        elif t == 2:
            follow[a-1][b-1] = 0
        else:
            if follow[a-1][b-1] == 1 and follow[b-1][a-1] == 1:
                print("Yes")
            else:
                print("No")
