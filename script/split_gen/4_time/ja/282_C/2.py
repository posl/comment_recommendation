def main():
    N = int(input())
    S = input()
    cnt = 0
    for i in range(N):
        if S[i] == '"':
            cnt += 1
        elif S[i] == ',':
            if cnt % 2 == 0:
                print('.', end='')
            else:
                print(',', end='')
        else:
            print(S[i], end='')
    print()
