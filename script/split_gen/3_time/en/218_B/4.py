def main():
    P = input().split()
    S = [''] * 26
    for i in range(26):
        S[int(P[i])-1] = chr(ord('a')+i)
    print(''.join(S))
