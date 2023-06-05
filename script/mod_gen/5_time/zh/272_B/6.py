def main():
    N, M = map(int, input().split())
    A = []
    for i in range(M):
        A.append(list(map(int, input().split())))
    flag = True
    for i in range(N):
        for j in range(i + 1, N):
            flag1 = False
            for k in range(M):
                if i + 1 in A[k] and j + 1 in A[k]:
                    flag1 = True
            if not flag1:
                flag = False
    if flag:
        print("Yes")
    else:
        print("No")
main()
