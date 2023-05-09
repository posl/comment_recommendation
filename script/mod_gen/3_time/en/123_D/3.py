def main():
    X, Y, Z, K = map(int, input().split())
    A = sorted(list(map(int, input().split())), reverse=True)
    B = sorted(list(map(int, input().split())), reverse=True)
    C = sorted(list(map(int, input().split())), reverse=True)
    lst = []
    for i in range(X):
        for j in range(Y):
            lst.append(A[i] + B[j])
    lst = sorted(lst, reverse=True)
    lst = lst[:K]
    lst2 = []
    for i in range(len(lst)):
        for j in range(Z):
            lst2.append(lst[i] + C[j])
    lst2 = sorted(lst2, reverse=True)
    for i in range(K):
        print(lst2[i])

if __name__ == '__main__':
    main()