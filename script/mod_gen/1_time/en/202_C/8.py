def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    #Bの各要素に対して、Cの何番目にあるかを記録しておく
    C_dict = {}
    for i in range(N):
        if B[C[i] - 1] in C_dict:
            C_dict[B[C[i] - 1]].append(i + 1)
        else:
            C_dict[B[C[i] - 1]] = [i + 1]
    #Aの各要素に対して、Cの何番目にあるかを記録しておく
    A_dict = {}
    for i in range(N):
        if A[i] in C_dict:
            if A[i] in A_dict:
                A_dict[A[i]].extend(C_dict[A[i]])
            else:
                A_dict[A[i]] = C_dict[A[i]]
    #A_dictの各要素に対して、Cの何番目にあるかを記録しておく
    ans = 0
    for i in range(N):
        if A[i] in A_dict:
            ans += len(A_dict[A[i]])
    print(ans)

if __name__ == '__main__':
    main()