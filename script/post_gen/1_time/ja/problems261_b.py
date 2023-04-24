Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == 'W' and A[j][i] != 'L':
                print('incorrect')
                return
            if A[i][j] == 'L' and A[j][i] != 'W':
                print('incorrect')
                return
            if A[i][j] == 'D' and A[j][i] != 'D':
                print('incorrect')
                return
    print('correct')

=======
Suggestion 2

def main():
    N = int(input())
    A = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                if A[i][j] != "-":
                    print("incorrect")
                    return
            else:
                if A[i][j] == "W" and A[j][i] != "L":
                    print("incorrect")
                    return
                elif A[i][j] == "L" and A[j][i] != "W":
                    print("incorrect")
                    return
                elif A[i][j] == "D" and A[j][i] != "D":
                    print("incorrect")
                    return
    print("correct")

=======
Suggestion 3

def main():
    N = int(input())
    A = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                if A[i][j] != "-":
                    print("incorrect")
                    return
            else:
                if A[i][j] == "W":
                    if A[j][i] != "L":
                        print("incorrect")
                        return
                elif A[i][j] == "L":
                    if A[j][i] != "W":
                        print("incorrect")
                        return
                elif A[i][j] == "D":
                    if A[j][i] != "D":
                        print("incorrect")
                        return
    print("correct")
main()

=======
Suggestion 4

def main():
    N = int(input())
    A = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                if A[i][j] != '-':
                    print("incorrect")
                    return
            else:
                if A[i][j] == 'W':
                    if A[j][i] != 'L':
                        print("incorrect")
                        return
                elif A[i][j] == 'L':
                    if A[j][i] != 'W':
                        print("incorrect")
                        return
                elif A[i][j] == 'D':
                    if A[j][i] != 'D':
                        print("incorrect")
                        return
    print("correct")
    return

=======
Suggestion 5

def main():
    N = int(input())
    A = [input() for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == "W" and A[j][i] != "L":
                print("incorrect")
                return
            if A[i][j] == "L" and A[j][i] != "W":
                print("incorrect")
                return
            if A[i][j] == "D" and A[j][i] != "D":
                print("incorrect")
                return
    print("correct")

=======
Suggestion 6

def main():
    N = int(input())
    A = [input() for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                if A[i][j] != "-":
                    print("incorrect")
                    return
            else:
                if A[i][j] == "W" and A[j][i] != "L":
                    print("incorrect")
                    return
                elif A[i][j] == "L" and A[j][i] != "W":
                    print("incorrect")
                    return
                elif A[i][j] == "D" and A[j][i] != "D":
                    print("incorrect")
                    return
    print("correct")

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    for i in range(N):
        for j in range(N):
            if i == j:
                if A[i][j] != "-":
                    print("incorrect")
                    return
            else:
                if A[i][j] == "W" and A[j][i] == "L":
                    print("incorrect")
                    return
                if A[i][j] == "L" and A[j][i] == "W":
                    print("incorrect")
                    return
                if A[i][j] == "D" and A[j][i] == "D":
                    print("incorrect")
                    return
    print("correct")

=======
Suggestion 8

def main():
    N = int(input())
    A = [input() for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j: continue
            if A[i][j] == "W" and A[j][i] != "L":
                print("incorrect")
                return
            if A[i][j] == "L" and A[j][i] != "W":
                print("incorrect")
                return
            if A[i][j] == "D" and A[j][i] != "D":
                print("incorrect")
                return
    print("correct")

=======
Suggestion 9

def main():
    # 入力
    N = int(input())
    A = [input() for _ in range(N)]
    # 処理
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == "W" and A[j][i] != "L":
                print("incorrect")
                return
            if A[i][j] == "L" and A[j][i] != "W":
                print("incorrect")
                return
            if A[i][j] == "D" and A[j][i] != "D":
                print("incorrect")
                return
    # 出力
    print("correct")
