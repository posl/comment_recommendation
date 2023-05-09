def main():
    P = list(map(int, input().split()))
    S = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(26):
        print(S[P[i]-1], end='')
    print()
