def main():
    S = input()
    T = input()
    lenT = len(T)
    lenS = len(S)
    for i in range(lenS - lenT + 1):
        flag = True
        for j in range(lenT):
            if S[i + j] != T[j] and S[i + j] != '?':
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')
