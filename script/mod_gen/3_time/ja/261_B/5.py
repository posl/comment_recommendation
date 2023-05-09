def main():
    N = int(input())
    A = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and A[i][j] == "W" and A[j][i] != "L":
                print("incorrect")
                return
            if i != j and A[i][j] == "L" and A[j][i] != "W":
                print("incorrect")
                return
            if i != j and A[i][j] == "D" and A[j][i] != "D":
                print("incorrect")
                return
    print("correct")
main()

if __name__ == '__main__':
    main()