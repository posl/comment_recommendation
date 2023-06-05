def main():
    N = int(input())
    S = input()
    for i in range(0, N, 2):
        if S[i] != '"' or S[i+1] != '"':
            S = S[:i] + '.' + S[i+1:]
    print(S)
