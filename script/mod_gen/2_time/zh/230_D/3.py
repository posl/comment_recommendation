def main():
    N, D = map(int, input().split())
    L_list = []
    R_list = []
    for i in range(N):
        L, R = map(int, input().split())
        L_list.append(L)
        R_list.append(R)
    L_list.sort()
    R_list.sort()
    # print(L_list)
    # print(R_list)
    if D == 1:
        print(N)
        return
    ans = 0
    L_index = 0
    R_index = 0
    while L_index < N:
        if L_list[L_index] == R_list[R_index]:
            L_index += 1
            R_index += 1
            continue
        if L_list[L_index] < R_list[R_index]:
            ans += 1
            L_index += 1
        else:
            ans -= 1
            R_index += 1
        if ans > D:
            print(ans)
            return
    print(ans)

if __name__ == '__main__':
    main()