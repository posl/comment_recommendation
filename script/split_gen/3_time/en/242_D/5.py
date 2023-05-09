def main():
    S = str(input())
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        print(solve(S, t, k))
