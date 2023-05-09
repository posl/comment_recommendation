def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append([int(x) for x in input().split()])
        for j in range(A[i][0]):
            A[i].append([int(x) for x in input().split()])
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(N):
            if i >> j & 1:
                for k in range(A[j][0]):
                    if A[j][k+1][1] == 1 and not i >> A[j][k+1][0]-1 & 1:
                        flag = False
                        break
                    if A[j][k+1][1] == 0 and i >> A[j][k+1][0]-1 & 1:
                        flag = False
                        break
        if flag:
            ans = max(ans, bin(i).count('1'))
    print(ans)

if __name__ == '__main__':
    main()