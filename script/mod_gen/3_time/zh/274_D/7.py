def solve():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, x, y)
    #print(A)
    #print(len(A))
    if len(A) != N:
        print("No")
        return
    A.append(0)
    A.append(0)
    for i in range(0, N+1):
        for j in range(i+1, N+2):
            if i == j:
                continue
            for k in range(j+1, N+3):
                if j == k:
                    continue
                #print(i, j, k)
                if check(A[i], A[j], A[k], x, y):
                    print("Yes")
                    return
    print("No")
    return

if __name__ == '__main__':
    solve()