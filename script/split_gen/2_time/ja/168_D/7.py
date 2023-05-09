def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = [0] * N
    ans[0] = -1
    ans[1] = 1
    for a, b in AB:
        if ans[a-1] == 0:
            ans[a-1] = b
        if ans[b-1] == 0:
            ans[b-1] = a
    if 0 in ans:
        print("No")
    else:
        print("Yes")
        for i in range(1, N):
            print(ans[i])
