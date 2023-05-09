def main():
    N = int(input())
    S = input()
    cnt = 0
    for i in range(N):
        if S[i] == '"':
            cnt += 1
        elif S[i] == ',' and cnt % 2 == 0:
            S = S[:i] + '.' + S[i+1:]
    print(S)
