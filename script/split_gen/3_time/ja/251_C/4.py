def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        s = s.strip()
        t = int(t)
        S.append(s)
        T.append(t)
    ans = 0
    for i in range(N):
        flag = 0
        for j in range(i):
            if S[i] == S[j]:
                flag = 1
                break
        if flag == 0:
            ans = i
    print(ans + 1)
