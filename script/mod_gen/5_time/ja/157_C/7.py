def check(N, M, s, c):
    for i in range(M):
        if N < s[i]:
            return False
        if N == s[i] and c[i] != 0:
            return False
    return True
N, M = map(int, input().split())
s = []
c = []
for i in range(M):
    s_i, c_i = map(int, input().split())
    s.append(s_i)
    c.append(c_i)
for i in range(10 ** (N - 1), 10 ** N):
    if check(str(i), M, s, c):
        print(i)
        exit()
print(-1)

if __name__ == '__main__':
    check()