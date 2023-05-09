def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s,t = input().split()
        S.append(s)
        T.append(int(t))
    ans = 0
    for i in range(N):
        flag = 0
        for j in range(i):
            if S[i] == S[j]:
                flag = 1
                break
        if flag == 0:
            if ans == 0:
                ans = i+1
            else:
                if T[ans-1] < T[i]:
                    ans = i+1
    print(ans)
