def is_ok():
    for i in range(N):
        if S[i] == T[i]:
            return False
        for j in range(i+1, N):
            if S[i] == T[j] or T[i] == S[j]:
                return False
    return True
N = int(input())
S, T = [], []
for i in range(N):
    s, t = input().split()
    S.append(s)
    T.append(t)

if __name__ == '__main__':
    is_ok()