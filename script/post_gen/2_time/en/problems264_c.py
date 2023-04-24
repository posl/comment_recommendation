Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            if A[i][j] == B[0][0]:
                for k in range(H2):
                    if A[i + k][j: j + W2] != B[k]:
                        break
                else:
                    print("Yes")
                    return
    print("No")
    return

=======
Suggestion 2

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    if H1 < H2 or W1 < W2:
        print("No")
        return
    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            if sum([A[i+k][j:j+W2] for k in range(H2)], []) == sum(B, []):
                print("Yes")
                return
    print("No")

=======
Suggestion 3

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]

    # Aの各行の和を計算
    Asum = [0] * H1
    for i in range(H1):
        Asum[i] = sum(A[i])
    # Bの各行の和を計算
    Bsum = [0] * H2
    for i in range(H2):
        Bsum[i] = sum(B[i])

    # Aの各行の和とBの各行の和が一致しているかどうかを判定
    Asum.sort()
    Bsum.sort()
    if Asum == Bsum:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]

    for h in range(H1 - H2 + 1):
        for w in range(W1 - W2 + 1):
            if A[h][w] == B[0][0]:
                for i in range(H2):
                    for j in range(W2):
                        if A[h + i][w + j] != B[i][j]:
                            break
                    else:
                        continue
                    break
                else:
                    print('Yes')
                    return
    print('No')

=======
Suggestion 5

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            if all(A[i + k][j + l] == B[k][l] for k in range(H2) for l in range(W2)):
                print('Yes')
                return
    print('No')

=======
Suggestion 6

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    if H1 < H2 or W1 < W2:
        print("No")
        return
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            flag = True
            for k in range(H2):
                for l in range(W2):
                    if A[i + k][j + l] != B[k][l]:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                print("Yes")
                return
    print("No")

=======
Suggestion 7

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            if B[0][0] == A[i][j]:
                for k in range(H2):
                    for l in range(W2):
                        if B[k][l] != A[i + k][j + l]:
                            break
                    else:
                        continue
                    break
                else:
                    print("Yes")
                    return
    print("No")

=======
Suggestion 8

def main():
    H1, W1 = map(int, input().split())
    A = []
    for _ in range(H1):
        A.append(list(map(int, input().split())))
    H2, W2 = map(int, input().split())
    B = []
    for _ in range(H2):
        B.append(list(map(int, input().split())))
    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            if A[i][j] == B[0][0]:
                flag = True
                for k in range(H2):
                    for l in range(W2):
                        if A[i+k][j+l] != B[k][l]:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    print("Yes")
                    return
    print("No")

=======
Suggestion 9

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

=======
Suggestion 10

def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()

    def solve():
        h1, w1 = map(int, input().split())
        a = [list(map(int, input().split())) for _ in range(h1)]
        h2, w2 = map(int, input().split())
        b = [list(map(int, input().split())) for _ in range(h2)]
        for i in range(h1 - h2 + 1):
            for j in range(w1 - w2 + 1):
                flag = True
                for k in range(h2):
                    for l in range(w2):
                        if a[i + k][j + l] != b[k][l]:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    print('Yes')
                    return
        print('No')

    solve()
