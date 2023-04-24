Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    C = []
    for i in range(N):
        if i % 2 == 0:
            B.append(i + 1)
        else:
            C.append(i + 1)
    print("Yes")
    print(len(B), *B)
    print(len(C), *C)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * 200
    C = [0] * 200
    for i in range(N):
        B[A[i] % 200] += 1
    for i in range(200):
        if B[i] >= 2:
            print("Yes")
            print(B[i], end=" ")
            for j in range(N):
                if A[j] % 200 == i:
                    print(j + 1, end=" ")
                    B[i] -= 1
                    if B[i] == 0:
                        break
            print()
            print(B[i], end=" ")
            for j in range(N):
                if A[j] % 200 == i:
                    print(j + 1, end=" ")
                    B[i] -= 1
                    if B[i] == 0:
                        break
            print()
            return
    print("No")

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int,input().split()))
    mod = [ [] for i in range(200) ]
    for i in range(N):
        mod[A[i]%200].append(i+1)
    for i in range(200):
        if len(mod[i]) >= 2:
            print("Yes")
            print(len(mod[i]),*mod[i])
            print(len(mod[i])-1,*mod[i][:-1])
            return
    print("No")

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    dp = [[-1] * mod for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(mod):
            if dp[i][j] != -1:
                dp[i + 1][j] = dp[i][j]
            elif dp[i + 1][(j + A[i]) % mod] != -1:
                dp[i + 1][j] = i + 1
            else:
                dp[i + 1][j] = -1
    if dp[N][0] == -1:
        print('No')
        return
    print('Yes')
    B = []
    C = []
    i = N
    j = 0
    while i != 0:
        if dp[i][j] == i:
            B.append(i)
            j = (j - A[i - 1]) % mod
        else:
            C.append(i)
        i -= 1
    B.reverse()
    C.reverse()
    print(len(B), *B)
    print(len(C), *C)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [(x % 200, i) for i, x in enumerate(A)]
    A.sort()
    for i in range(N-1):
        if A[i][0] == A[i+1][0]:
            print("Yes")
            print(i+1, A[i][1]+1, A[i+1][1]+1)
            print(N-i-1, A[i+2][1]+1, A[i+3][1]+1)
            return
    print("No")

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    mod_dict = {}
    for i in range(N):
        mod_dict[i] = A[i] % mod
    for i in range(N):
        for j in range(i+1, N):
            if mod_dict[i] == mod_dict[j]:
                print("Yes")
                print("1 {}".format(i+1))
                print("1 {}".format(j+1))
                return
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if mod_dict[i] == mod_dict[j] == mod_dict[k]:
                    print("Yes")
                    print("2 {} {}".format(i+1, j+1))
                    print("1 {}".format(k+1))
                    return
    print("No")

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    modA = [a % mod for a in A]
    modA_set = set(modA)
    if len(modA_set) == N:
        print("No")
        return
    print("Yes")
    modA_dict = {}
    for i, a in enumerate(modA):
        if a in modA_dict:
            modA_dict[a].append(i+1)
        else:
            modA_dict[a] = [i+1]
    for a in modA_dict:
        if len(modA_dict[a]) > 1:
            x = len(modA_dict[a])
            print(x, *modA_dict[a])
            break
    y = N - x
    C = []
    for i in range(N):
        if i+1 not in modA_dict[a]:
            C.append(i+1)
    print(y, *C)

main()

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 200で割った余りでグループ分け
    g = [[] for _ in range(200)]
    for i, x in enumerate(a):
        g[x % 200].append(i + 1)
    # 余りが等しい組み合わせがあれば出力
    for x in g:
        if len(x) >= 2:
            print('Yes')
            print(1, x[0])
            print(1, x[1])
            return
    # 余りが等しい組み合わせがなければ、
    # 余りが等しい数列を2つ作る
    for i in range(200):
        for j in range(i + 1, 200):
            if len(g[i]) >= 1 and len(g[j]) >= 1:
                print('Yes')
                print(len(g[i]), *g[i])
                print(len(g[j]), *g[j])
                return
    print('No')

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 余りをキーとして、Aのインデックスを値とする辞書を作成
    # 余りが重複する場合は、インデックスを追加
    remainder = {}
    for i, a in enumerate(A):
        if a % 200 in remainder:
            remainder[a % 200].append(i)
        else:
            remainder[a % 200] = [i]

    # 余りが重複しているものがあれば、それを出力
    for r in remainder:
        if len(remainder[r]) > 1:
            print("Yes")
            print(1, remainder[r][0] + 1)
            print(1, remainder[r][1] + 1)
            exit()

    # 余りが重複していない場合
    # 余りの組み合わせを作成
    # 余りが重複している場合と同様に、インデックスを追加
    combinations = {}
    for r1 in remainder:
        for r2 in remainder:
            if r1 == r2:
                continue
            if (r1 + r2) % 200 in combinations:
                combinations[(r1 + r2) % 200].append([r1, r2])
            else:
                combinations[(r1 + r2) % 200] = [[r1, r2]]

    # 余りの組み合わせが重複しているものがあれば、それを出力
    for c in combinations:
        if len(combinations[c]) > 1:
            print("Yes")
            print(len(remainder[combinations[c][0][0]]), *list(map(lambda x: x + 1, remainder[combinations[c][0][0]])))
            print(len(remainder[combinations[c][0][1]]), *list(map(lambda x: x + 1, remainder[combinations[c][0][1]])))
            exit()

    # 余りの組み合わせが重複してい

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]

    # 2つの数列の組み合わせがあるか
    # 1つの数列の中に200の倍数があるか
    # 2つの数列の中に200の倍数があるか
    # それ以外
    # という3つの場合に分けて考える

    # 1つの数列の中に200の倍数がある場合
    for i in range(N):
        if A[i] % 200 == 0:
            print('Yes')
            print(1)
            print(i+1)
            print(1)
            print(i+1)
            return

    # 2つの数列の中に200の倍数がある場合
    for i in range(N):
        for j in range(i+1,N):
            if (A[i] + A[j]) % 200 == 0:
                print('Yes')
                print(1)
                print(i+1)
                print(2)
                print(i+1, j+1)
                return

    # それ以外
    # 1つの数列の中に200の倍数がない場合
    # 2つの数列の中に200の倍数がない場合
    # 2つの数列の中に200の倍数がある場合
    # という4つの場合に分けて考える

    # 2つの数列の中に200の倍数がある場合
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if (A[i] + A[j] + A[k]) % 200 == 0:
                    print('Yes')
                    print(2)
                    print(i+1, j+1)
                    print(1)
                    print(k+1)
                    return

    # 1つの数列の中に200の倍数がない場合
    # 2つの数列の中に200
