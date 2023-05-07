def main():
    N, M = map(int, input().split())
    if N == 1:
        if M == 0:
            print(0)
            return
        else:
            s, c = map(int, input().split())
            if s == 1 and c == 0:
                print(-1)
            else:
                print(c)
            return
    else:
        s = []
        c = []
        for _ in range(M):
            s_i, c_i = map(int, input().split())
            s.append(s_i)
            c.append(c_i)
        ans = [0] * N
        for i in range(N):
            ans[i] = 1
        for i in range(M):
            ans[s[i] - 1] = c[i]
        if ans[0] == 1:
            ans[0] = 2
        print("".join(map(str, ans)))
