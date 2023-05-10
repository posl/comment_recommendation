def main():
    N = int(input())
    S = input()
    ans = [0] * N
    cnt = 0
    for i in range(N):
        if S[i] == '"':
            cnt += 1
        if S[i] == ',':
            if cnt % 2 == 0:
                ans[i] = 1
    for i in range(N):
        if ans[i] == 1:
            print('.', end='')
        else:
            print(S[i], end='')
    print()

if __name__ == '__main__':
    main()