def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(2 ** N):
        flag = True
        for j in range(M):
            if (i >> (A[j] - 1)) % 2 == 1 and (i >> (B[j] - 1)) % 2 == 1:
                flag = False
                break
        if flag:
            print("Yes")
            return
    print("No")
    return

if __name__ == '__main__':
    main()