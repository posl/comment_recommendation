def main():
    N = int(input())
    S = input()
    for i in range(N):
        if S[i] == ',':
            if i%2 == 0:
                S = S[:i] + '.' + S[i+1:]
    print(S)
