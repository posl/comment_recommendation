def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S1 = S[:i]
        S2 = S[-(len(T)-i):]
        if S1.count('?') + S2.count('?') == len(T):
            print('Yes')
        else:
            print('No')
