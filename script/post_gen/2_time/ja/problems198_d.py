Synthesizing 8/10 solutions

=======
Suggestion 1

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    N1 = len(S1)
    N2 = len(S2)
    N3 = len(S3)
    if N1 < N2:
        S1, S2 = S2, S1
        N1, N2 = N2, N1
    if N1 < N3:
        S1, S3 = S3, S1
        N1, N3 = N3, N1
    if N2 < N3:
        S2, S3 = S3, S2
        N2, N3 = N3, N2

    D = {}
    for i in range(N1):
        D[S1[i]] = 0
    for i in range(N2):
        D[S2[i]] = 0
    for i in range(N3):
        D[S3[i]] = 0
    #print(D)
    #print(N1, N2, N3)

    if N1 == N3:
        for i in range(10):
            if S1[0] == S3[0] and i == 0:
                continue
            if S2[0] == S3[0] and i == 0:
                continue
            D[S1[0]] = i
            for j in range(10):
                if S1[1] == S3[1] and j == 0:
                    continue
                if S2[1] == S3[1] and j == 0:
                    continue
                D[S2[0]] = j
                for k in range(10):
                    if S1[2] == S3[2] and k == 0:
                        continue
                    if S2[2] == S3[2] and k == 0:
                        continue
                    D[S3[0]] = k
                    #print(D)
                    if D[S1[0]] + D[S2[0]] == D[S3[0]]:
                        if D[S1[1]] + D[S2[1]] == D[S3[1]]:
                            if D[S1[2]] + D[S2[2]] == D[S3[2]]:
                                print(D[S1[0]]*100+D[S1

=======
Suggestion 2

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    N1 = len(S1)
    N2 = len(S2)
    N3 = len(S3)
    if N1 < N2 or N1 < N3:
        print("UNSOLVABLE")
        return
    if N1 == N2:
        if N1 == N3:
            if S1 == S2 and S1 != S3:
                print("UNSOLVABLE")
                return
            if S1 != S2 and S1 == S3:
                print("UNSOLVABLE")
                return
            if S1 == S3 and S1 != S2:
                print("UNSOLVABLE")
                return
        else:
            if S1 == S2:
                print("UNSOLVABLE")
                return
    else:
        if N1 == N3:
            if S1 == S3:
                print("UNSOLVABLE")
                return
        else:
            if N2 == N3:
                if S2 == S3:
                    print("UNSOLVABLE")
                    return
    if N1 == N3:
        if N1 == N2:
            if S1 == S3 and S1 != S2:
                print("UNSOLVABLE")
                return
            if S1 != S3 and S1 == S2:
                print("UNSOLVABLE")
                return
            if S1 == S2 and S1 != S3:
                print("UNSOLVABLE")
                return
        else:
            if S1 == S3:
                print("UNSOLVABLE")
                return
    else:
        if N1 == N2:
            if S1 == S2:
                print("UNSOLVABLE")
                return
        else:
            if N2 == N3:
                if S2 == S3:
                    print("UNSOLVABLE")
                    return
    if N1 == N2:
        if N1 == N3:
            if S1 == S2 and S1 == S3:
                print("UNSOLVABLE")
                return
    else:
        if N1 == N3:
            if S1 == S3:
                print("UNSOLVABLE")
                return
        else:
            if N2 == N3:
                if S

=======
Suggestion 3

def solve():
    S1 = input()
    S2 = input()
    S3 = input()
    N1 = len(S1)
    N2 = len(S2)
    N3 = len(S3)
    if N1 < N3 and N2 < N3:
        print("UNSOLVABLE")
        return

    def check(S1,S2,S3):
        for i in range(len(S1)):
            if S1[i] == S2[i] and S1[i] != S3[i]:
                return False
            if S1[i] == S3[i] and S1[i] != S2[i]:
                return False
            if S2[i] == S3[i] and S1[i] != S2[i]:
                return False
        return True

    def solve(S1,S2,S3):
        ans = []
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    if S1[0] == "0" and i == 0:
                        continue
                    if S2[0] == "0" and j == 0:
                        continue
                    if S3[0] == "0" and k == 0:
                        continue
                    S1_ = str(i)*N1
                    S2_ = str(j)*N2
                    S3_ = str(k)*N3
                    if check(S1_,S2_,S3_):
                        ans.append((S1_,S2_,S3_))
        return ans

    ans = solve(S1,S2,S3)
    if len(ans) == 0:
        print("UNSOLVABLE")
    else:
        print(ans[0][0])
        print(ans[0][1])
        print(ans[0][2])

=======
Suggestion 4

def solve():
    S1 = input()
    S2 = input()
    S3 = input()
    if len(S1) != len(S2) or len(S2) != len(S3):
        print("UNSOLVABLE")
        exit()
    if len(set(S1)) > 10 or len(set(S2)) > 10 or len(set(S3)) > 10:
        print("UNSOLVABLE")
        exit()
    N1 = []
    N2 = []
    N3 = []
    for i in range(len(S1)):
        N1.append(S1[i])
        N2.append(S2[i])
        N3.append(S3[i])
    N1 = set(N1)
    N2 = set(N2)
    N3 = set(N3)
    if len(N1) > 10 or len(N2) > 10 or len(N3) > 10:
        print("UNSOLVABLE")
        exit()
    if len(N1) + len(N2) + len(N3) > 10:
        print("UNSOLVABLE")
        exit()
    N1 = list(N1)
    N2 = list(N2)
    N3 = list(N3)
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if i in N1 or j in N2 or k in N3:
                    continue
                if len(N1) == 1:
                    if N1[0] == S1[0] and i == 0:
                        continue
                if len(N2) == 1:
                    if N2[0] == S2[0] and j == 0:
                        continue
                if len(N3) == 1:
                    if N3[0] == S3[0] and k == 0:
                        continue
                for l in range(len(S1)):
                    if S1[l] == N1[0]:
                        S1 = S1.replace(S1[l], str(i))
                    if S2[l] == N2[0]:
                        S2 = S2.replace(S2[l], str(j))
                    if S3[l] == N3[0]:
                        S3 = S3.replace(S3[l], str(k))
                if int(S1) + int(S2) == int(S3):

=======
Suggestion 5

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    if len(S1) < len(S3) and len(S2) < len(S3):
        print("UNSOLVABLE")
    else:
        N1 = 0
        N2 = 0
        N3 = 0
        for i in range(len(S1)):
            N1 += (ord(S1[i]) - ord("a") + 1) * 10 ** (len(S1) - i - 1)
        for i in range(len(S2)):
            N2 += (ord(S2[i]) - ord("a") + 1) * 10 ** (len(S2) - i - 1)
        for i in range(len(S3)):
            N3 += (ord(S3[i]) - ord("a") + 1) * 10 ** (len(S3) - i - 1)
        if N1 + N2 == N3:
            print(N1)
            print(N2)
            print(N3)
        else:
            print("UNSOLVABLE")

main()

=======
Suggestion 6

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = S1 + S2 + S3
    S = set(S)
    L = len(S)
    if L > 10:
        print("UNSOLVABLE")
        return

    from itertools import permutations
    for p in permutations(range(10), L):
        d = dict(zip(S, p))
        if d[S1[0]] == 0 or d[S2[0]] == 0 or d[S3[0]] == 0:
            continue
        if int(S1.translate(str.maketrans(d))) + int(S2.translate(str.maketrans(d))) == int(S3.translate(str.maketrans(d))):
            print(int(S1.translate(str.maketrans(d))))
            print(int(S2.translate(str.maketrans(d))))
            print(int(S3.translate(str.maketrans(d))))
            return
    print("UNSOLVABLE")

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()
    s3 = input()

    #文字列の長さが違う場合は解けない
    if len(s1) != len(s2) or len(s2) != len(s3):
        print('UNSOLVABLE')
        return

    #文字列の文字数をカウント
    c1 = [0]*26
    c2 = [0]*26
    c3 = [0]*26
    for i in range(len(s1)):
        c1[ord(s1[i])-97] += 1
        c2[ord(s2[i])-97] += 1
        c3[ord(s3[i])-97] += 1

    #文字列の文字数が同じであるかチェック
    for i in range(26):
        if c1[i] != c2[i] or c1[i] != c3[i]:
            print('UNSOLVABLE')
            return

    #各文字列の先頭文字が0の場合は解けない
    if s1[0] == '0' or s2[0] == '0' or s3[0] == '0':
        print('UNSOLVABLE')
        return

    #文字列を数字に変換
    n1 = int(s1)
    n2 = int(s2)
    n3 = int(s3)

    #各文字列の先頭文字を1~9に置換して試す
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,10):
                if s1.count(str(i)) == 1 and s2.count(str(j)) == 1 and s3.count(str(k)) == 1:
                    if n1 - n1//10*10 == i and n2 - n2//10*10 == j and n3 - n3//10*10 == k:
                        if n1 + n2 == n3:
                            print(n1)
                            print(n2)
                            print(n3)
                            return

    print('UNSOLVABLE')

=======
Suggestion 8

def main():
  s1 = input()
  s2 = input()
  s3 = input()
  # 重複文字を除く
  # set関数は集合を作成する関数
  # 例えば、set('abc')は、{'a', 'c', 'b'}という集合を作成する
  # 重複文字を除くために、set関数を使用する
  # また、set関数によって、文字列はリストに変換される
  # 例えば、set('abc')は、['a', 'c', 'b']というリストに変換される
  # そのため、set関数を使用すると、文字列をリストに変換することが可能
  # また、set関数によって、文字列はリストに変換される
  # 例えば、set('abc')は、['a', 'c', 'b']というリストに変換される
  # そのため、set関数を使用すると、文字列をリストに変換することが可能
  # また、set関数によって、文字列はリストに変換される
  # 例えば、set('abc')は、['a', 'c', 'b']というリストに変換される
  # そのため、set関数を使用すると、文字列をリストに変換することが可能
  # また、set関数によって、文字列はリストに変換される
  # 例えば、set('abc')は、['a', 'c', 'b']というリストに変換される
  # そのため、set関数を使用すると、文字列をリストに変換することが可能
  # また、set関数によって、文字列はリストに変換される
  # 例えば、set('abc')は、['a
