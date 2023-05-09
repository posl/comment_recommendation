def main():
    N = int(input())
    intervals = []
    for i in range(N):
        L, R = map(int, input().split())
        intervals.append((L, R))
    intervals.sort(key=lambda x: x[0])
    ans = []
    for L, R in intervals:
        if not ans or ans[-1][1] < L:
            ans.append((L, R))
        else:
            ans[-1] = (ans[-1][0], max(ans[-1][1], R))
    for L, R in ans:
        print(L, R)
