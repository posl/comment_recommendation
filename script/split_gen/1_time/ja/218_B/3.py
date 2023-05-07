def main():
    P = list(map(int,input().split()))
    S = [chr(ord('a') + i) for i in range(26)]
    for i in range(26):
        S[P[i] - 1] = chr(ord('a') + i)
    print(''.join(S))
