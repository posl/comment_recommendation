def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    S.append("")
    c = 1
    for i in range(N):
        if S[i] != S[i+1]:
            if c > 1:
                print(S[i])
            c = 1
        else:
            c += 1
