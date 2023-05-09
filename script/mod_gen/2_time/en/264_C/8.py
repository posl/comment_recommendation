def main():
    H1, W1 = map(int, input().split())
    A = []
    for i in range(H1):
        A.append(list(map(int, input().split())))
    H2, W2 = map(int, input().split())
    B = []
    for i in range(H2):
        B.append(list(map(int, input().split())))
    #Aの各行の和とBの各行の和が等しくない場合はNo
    for i in range(H1):
        if sum(A[i]) != sum(B[i]):
            print("No")
            return
    #Aの各列の和とBの各列の和が等しくない場合はNo
    for i in range(W1):
        sumA = 0
        sumB = 0
        for j in range(H1):
            sumA += A[j][i]
            sumB += B[j][i]
        if sumA != sumB:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()