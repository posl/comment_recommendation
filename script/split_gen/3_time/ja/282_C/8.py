def main():
    N = int(input())
    S = input()
    if S.count('"') % 2 == 1:
        print('error')
        return
    cnt = 0
    for i in range(N):
        if S[i] == '"':
            cnt += 1
        elif S[i] == ',' and cnt % 2 == 1:
            print('.', end='')
        else:
            print(S[i], end='')
    print()
