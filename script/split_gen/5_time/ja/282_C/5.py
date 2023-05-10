def main():
    N = int(input())
    S = input()
    cnt = 0
    for i in range(N):
        if S[i] == '"':
            cnt += 1
        elif S[i] == ',':
            if cnt % 2 == 1:
                S = S[:i] + '.' + S[i+1:]
    print(S)
