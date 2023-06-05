def main():
    S = input()
    T = input()
    n = len(S)
    m = len(T)
    for x in range(n - m + 1):
        flag = True
        for i in range(m):
            if S[x + i] != T[i] and S[x + i] != '?':
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')
