def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -float("inf")
    for i in range(N):
        x = i
        tmp = 0
        tmp_list = []
        tmp_list.append(C[x])
        tmp += C[x]
        x = P[x]-1
        while x != i:
            tmp_list.append(C[x])
            tmp += C[x]
            x = P[x]-1
        if tmp > 0:
            tmp_list = tmp_list*(K//len(tmp_list))+tmp_list[:K%len(tmp_list)]
            tmp = tmp*(K//len(tmp_list))+tmp*(K%len(tmp_list))
        else:
            tmp_list = tmp_list[:K]
            tmp = tmp*(K//len(tmp_list))+tmp*(K%len(tmp_list))
        ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()