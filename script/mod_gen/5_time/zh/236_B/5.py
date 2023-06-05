def solve():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for a in A:
        S[a] += 1
    for i in range(1, N + 1):
        if S[i] == 4:
            print(i)
            return
    for i in range(1, N + 1):
        if S[i] == 2:
            print(i)
            return

if __name__ == '__main__':
    solve()