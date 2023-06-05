def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    ans = []
    for i in range(N):
        if A[i][0] == 1:
            ans.append(A[i][1])
        elif A[i][0] == 2:
            tmp = []
            for j in range(len(ans)):
                if ans[j] == A[i][1]:
                    tmp.append(j)
            for j in range(A[i][2]):
                ans.pop(tmp.pop())
        elif A[i][0] == 3:
            print(max(ans) - min(ans))

if __name__ == '__main__':
    main()