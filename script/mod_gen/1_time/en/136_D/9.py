def main():
    S = input()
    N = len(S)
    ans = [0] * N
    #Lが現れるときまでのRの数を数える
    cnt = 0
    for i, s in enumerate(S):
        if s == 'R':
            cnt += 1
        else:
            ans[i] += (cnt + 1) // 2
            ans[i - 1] += cnt // 2
            cnt = 0
    #Rが現れるときまでのLの数を数える
    cnt = 0
    for i in range(N - 1, -1, -1):
        if S[i] == 'L':
            cnt += 1
        else:
            ans[i] += (cnt + 1) // 2
            ans[i + 1] += cnt // 2
            cnt = 0
    print(' '.join(map(str, ans)))
main()

if __name__ == '__main__':
    main()