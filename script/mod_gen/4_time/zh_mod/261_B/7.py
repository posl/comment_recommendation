def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    for i in range(N):
        for j in range(N):
            if A[i][j] != A[j][i]:
                print("incorrect")
                return
    print("correct")
    return

if __name__ == '__main__':
    main()