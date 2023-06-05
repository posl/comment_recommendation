def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    mod = [0] * (N + 1)
    for i in range(N):
        mod[i + 1] = (mod[i] + A[i]) % M
    mod_dic = {}
    for i in mod:
        if i in mod_dic:
            mod_dic[i] += 1
        else:
            mod_dic[i] = 1
    ans = 0
    for i in mod_dic:
        ans += mod_dic[i] * (mod_dic[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()