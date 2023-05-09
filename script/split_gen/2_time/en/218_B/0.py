def main():
    P = list(map(int, input().split()))
    S = [''] * 26
    for i in range(26):
        S[P[i] - 1] = chr(i + 97)
    print(''.join(S))
