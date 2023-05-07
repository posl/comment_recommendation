def main():
    P = input()
    P = P.split(' ')
    P = [int(i) for i in P]
    S = ''
    for i in range(26):
        S += chr(P.index(i+1)+97)
    print(S)
