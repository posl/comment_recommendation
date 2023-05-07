def main():
    alphabet = input()
    N = int(input())
    S = [input() for i in range(N)]
    S.sort(key=lambda x: [alphabet.index(c) for c in x])
    print(*S, sep='
')
