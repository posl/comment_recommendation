def main():
    S = input()
    T = input()
    lenS = len(S)
    lenT = len(T)
    for i in range(lenS):
        if S[i] != T[i]:
            print('No')
            return
    print('Yes')
    return
