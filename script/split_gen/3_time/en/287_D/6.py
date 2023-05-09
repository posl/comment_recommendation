def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S1 = S[:i]
        S2 = S[-(len(T)-i):]
        S1 = S1.replace('?', 'a')
        S2 = S2.replace('?', 'a')
        if S1 + S2 == T:
            print('Yes')
        else:
            print('No')
    return
