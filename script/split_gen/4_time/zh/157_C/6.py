def main():
    N, M = map(int, input().split())
    s = []
    c = []
    for i in range(M):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)
    min_n = 10 ** (N - 1)
    max_n = 10 ** N - 1
    for n in range(min_n, max_n + 1):
        n = str(n)
        for i in range(M):
            if n[s[i] - 1] != str(c[i]):
                break
        else:
            print(n)
            break
    else:
        print(-1)
