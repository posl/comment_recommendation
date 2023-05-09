def main():
    N, M = map(int, input().split())
    k = []
    a = []
    for i in range(M):
        k_i = int(input())
        k.append(k_i)
        a_i = list(map(int, input().split()))
        a.append(a_i)
    #print(N, M)
    #print(k)
    #print(a)
    #print("
")
    for i in range(M):
        for j in range(k[i]):
            a[i][j] = a[i][j] - 1
    #print(a)
    #print("
")
    for i in range(M):
        for j in range(k[i]):
            a[i][j] = a[i][j] + N * i
    #print(a)
    #print("
")
    for i in range(M):
        for j in range(k[i]):
            a[i][j] = a[i][j] + 1
    #print(a)
    #print("
")
    b = []
    for i in range(M):
        for j in range(k[i]):
            b.append(a[i][j])
    #print(b)
    #print("
")
    b.sort()
    #print(b)
    #print("
")
    for i in range(2 * N):
        if b[i] % N != b[i + 1] % N:
            print("No")
            return
    print("Yes")
    return
