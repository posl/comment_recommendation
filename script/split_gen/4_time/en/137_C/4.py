def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(sorted(input()))
    S.sort()
    cnt = 0
    tmp = 0
    for i in range(N):
        if S[i] == S[i-1]:
            cnt += tmp
            tmp += 1
        else:
            tmp = 1
    print(cnt)
main()
