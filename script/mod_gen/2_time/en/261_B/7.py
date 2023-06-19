def main():
    N = int(input())
    table = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                if table[i][j] != "-":
                    print("incorrect")
                    return
            else:
                if table[i][j] == "W":
                    if table[j][i] != "L":
                        print("incorrect")
                        return
                elif table[i][j] == "L":
                    if table[j][i] != "W":
                        print("incorrect")
                        return
                else:
                    if table[j][i] != "D":
                        print("incorrect")
                        return
    print("correct")
    return
main()
