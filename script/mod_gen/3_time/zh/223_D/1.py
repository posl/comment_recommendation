def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # 1. B中的数值不能出现在A中
    # 2. A中的数值不能出现在B中
    # 3. A中的数值不能出现在B中的前面
    # 4. B中的数值不能出现在A中的前面
    # 1. B中的数值不能出现在A中
    A_set = set(A)
    B_set = set(B)
    if len(B_set & A_set) > 0:
        print(-1)
        return
    # 2. A中的数值不能出现在B中
    if len(A_set & B_set) > 0:
        print(-1)
        return
    # 3. A中的数值不能出现在B中的前面
    # 4. B中的数值不能出现在A中的前面
    # 3. A中的数值不能出现在B中的前面
    # 4. B中的数值不能出现在A中的前面
    # 3. A中的数值不能出现在B中的前面
    # 4. B中的数值不能出现在A中的前面
    # 3. A中的数值不能出现在B中的前面
    # 4. B中的数值不能出现在A中的前面
    # 3. A中的数值不能出现在B中的前面
    # 4. B中的数值不能出现在A中的前面
    # 3. A中的数值不能出现在B中的前面
    # 4. B中的数值不能出现在A中的前面
    # 3. A中的数值不能出现在B中的前面
    # 4. B中的数值不能出现在A中的前面
    #

if __name__ == '__main__':
    main()