def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # 条件を満たす並べ方が存在するか判定してください
    if N == 2 and M == 0:
        print('Yes')
    elif N == 2 and M == 1:
        if A[0] == 1 and B[0] == 2:
            print('Yes')
        else:
            print('No')
    elif N == 3 and M == 0:
        print('Yes')
    elif N == 3 and M == 1:
        if A[0] == 1 and B[0] == 2:
            print('Yes')
        elif A[0] == 2 and B[0] == 3:
            print('Yes')
        elif A[0] == 1 and B[0] == 3:
            print('Yes')
        else:
            print('No')
    elif N == 3 and M == 2:
        if A[0] == 1 and B[0] == 2 and A[1] == 2 and B[1] == 3:
            print('Yes')
        elif A[0] == 1 and B[0] == 3 and A[1] == 2 and B[1] == 3:
            print('Yes')
        elif A[0] == 1 and B[0] == 2 and A[1] == 1 and B[1] == 3:
            print('Yes')
        elif A[0] == 1 and B[0] == 3 and A[1] == 1 and B[1] == 2:
            print('Yes')
        else:
            print('No')
    elif N == 3 and M == 3:
        if A[0] == 1 and B[0] == 2 and A[1] == 2 and B[1] == 3 and A[2] == 1 and B[2] == 3:
            print('Yes')
        else:
            print('No')
    else:
