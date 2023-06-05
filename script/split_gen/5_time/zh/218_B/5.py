def main():
    P = input().split(' ')
    P = [int(i) for i in P]
    S = [0]*26
    for i in range(26):
        S[P[i]-1] = chr(i+97)
    print(''.join(S))
