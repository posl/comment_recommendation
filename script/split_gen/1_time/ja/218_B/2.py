def main():
    P = list(map(int, input().split()))
    S = ''
    for i in range(26):
        S += chr(ord('a') + P.index(i+1))
    print(S)
