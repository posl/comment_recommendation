def main():
    N = int(input())
    A = [input() for _ in range(N)]
    ans = "correct"
    for i in range(N):
        for j in range(N):
            if i == j:
                if A[i][j] != "-":
                    ans = "incorrect"
                    break
            else:
                if A[i][j] == "W":
                    if A[j][i] != "L":
                        ans = "incorrect"
                        break
                elif A[i][j] == "L":
                    if A[j][i] != "W":
                        ans = "incorrect"
                        break
                elif A[i][j] == "D":
                    if A[j][i] != "D":
                        ans = "incorrect"
                        break
    print(ans)
main()

if __name__ == '__main__':
    main()