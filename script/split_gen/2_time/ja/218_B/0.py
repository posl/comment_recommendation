def main():
    P = list(map(int, input().split()))
    S = []
    for i in range(26):
        S.append(chr(ord('a') + P[i] - 1))
    print(''.join(S))
