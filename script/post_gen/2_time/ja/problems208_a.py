Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == B and A == 2:
                print('Yes')
                return
            for k in range(1, 7):
                if i + j + k == B and A == 3:
                    print('Yes')
                    return
                for l in range(1, 7):
                    if i + j + k + l == B and A == 4:
                        print('Yes')
                        return
                    for m in range(1, 7):
                        if i + j + k + l + m == B and A == 5:
                            print('Yes')
                            return
                        for n in range(1, 7):
                            if i + j + k + l + m + n == B and A == 6:
                                print('Yes')
                                return
                            for o in range(1, 7):
                                if i + j + k + l + m + n + o == B and A == 7:
                                    print('Yes')
                                    return
                                for p in range(1, 7):
                                    if i + j + k + l + m + n + o + p == B and A == 8:
                                        print('Yes')
                                        return
                                    for q in range(1, 7):
                                        if i + j + k + l + m + n + o + p + q == B and A == 9:
                                            print('Yes')
                                            return
                                        for r in range(1, 7):
                                            if i + j + k + l + m + n + o + p + q + r == B and A == 10:
                                                print('Yes')
                                                return
                                            for s in range(1, 7):
                                                if i + j + k + l + m + n + o + p + q + r + s == B and A == 11:
                                                    print('Yes')
                                                    return
                                                for t in range(1, 7):
                                                    if i + j + k + l + m + n + o + p + q + r + s + t == B and A == 12:
                                                        print('Yes')
                                                        return
                                                    for u in range(1, 7):
                                                        if

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == B and A == 2:
                print("Yes")
                exit()
            for k in range(1, 7):
                if i + j + k == B and A == 3:
                    print("Yes")
                    exit()
                for l in range(1, 7):
                    if i + j + k + l == B and A == 4:
                        print("Yes")
                        exit()
                    for m in range(1, 7):
                        if i + j + k + l + m == B and A == 5:
                            print("Yes")
                            exit()
                        for n in range(1, 7):
                            if i + j + k + l + m + n == B and A == 6:
                                print("Yes")
                                exit()
                            for o in range(1, 7):
                                if i + j + k + l + m + n + o == B and A == 7:
                                    print("Yes")
                                    exit()
                                for p in range(1, 7):
                                    if i + j + k + l + m + n + o + p == B and A == 8:
                                        print("Yes")
                                        exit()
                                    for q in range(1, 7):
                                        if i + j + k + l + m + n + o + p + q == B and A == 9:
                                            print("Yes")
                                            exit()
                                        for r in range(1, 7):
                                            if i + j + k + l + m + n + o + p + q + r == B and A == 10:
                                                print("Yes")
                                                exit()
                                            for s in range(1, 7):
                                                if i + j + k + l + m + n + o + p + q + r + s == B and A == 11:
                                                    print("Yes")
                                                    exit()
                                                for t in range(1, 7):
                                                    if i + j + k + l + m + n + o + p + q + r + s + t == B and A == 12:
                                                        print("Yes")
                                                        exit()
                                                    for u in range(1, 7):
                                                        if

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if A * 1 <= B <= A * 6:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if 1 <= A <= 100 and 1 <= B <= 1000:
        if A == 1 and B <= 6:
            print('Yes')
        elif A == 2 and B <= 12:
            print('Yes')
        elif A == 3 and B <= 18:
            print('Yes')
        elif A == 4 and B <= 24:
            print('Yes')
        elif A == 5 and B <= 30:
            print('Yes')
        elif A == 6 and B <= 36:
            print('Yes')
        elif A == 7 and B <= 42:
            print('Yes')
        elif A == 8 and B <= 48:
            print('Yes')
        elif A == 9 and B <= 54:
            print('Yes')
        elif A == 10 and B <= 60:
            print('Yes')
        elif A == 11 and B <= 66:
            print('Yes')
        elif A == 12 and B <= 72:
            print('Yes')
        elif A == 13 and B <= 78:
            print('Yes')
        elif A == 14 and B <= 84:
            print('Yes')
        elif A == 15 and B <= 90:
            print('Yes')
        elif A == 16 and B <= 96:
            print('Yes')
        elif A == 17 and B <= 102:
            print('Yes')
        elif A == 18 and B <= 108:
            print('Yes')
        elif A == 19 and B <= 114:
            print('Yes')
        elif A == 20 and B <= 120:
            print('Yes')
        elif A == 21 and B <= 126:
            print('Yes')
        elif A == 22 and B <= 132:
            print('Yes')
        elif A == 23 and B <= 138:
            print('Yes')
        elif A == 24 and B <= 144:
            print('Yes')
        elif A == 25 and B <= 150:
            print('Yes')
        elif A == 26 and B <= 156:
            print('Yes')
        elif A == 27 and B <= 162:
            print('Yes')
        elif A == 28 and B

=======
Suggestion 5

def main():
    # A, B = map(int, input().split())
    A, B = 100, 600
    for a in range(1, 7):
        for b in range(1, 7):
            if a + b == B:
                print("Yes")
                return
    print("No")

=======
Suggestion 6

def main():
    # A:サイコロを振る回数
    # B:出た目の合計
    A, B = map(int, input().split())
    # 1,2,...,6 の出目がある 6 面サイコロを A 回振ったとき、出た目の合計が B になることはありますか？
    # 1,2,...,6 の出目がある 6 面サイコロを A 回振ったとき、出た目の合計が B になることはありますか？
    # 1,2,...,6 の出目がある 6 面サイコロを A 回振ったとき、出た目の合計が B になることはありますか？
    # 1,2,...,6 の出目がある 6 面サイコロを A 回振ったとき、出た目の合計が B になることはありますか？
    # 1,2,...,6 の出目がある 6 面サイコロを A 回振ったとき、出た目の合計が B になることはありますか？
    # 1,2,...,6 の出目がある 6 面サイコロを A 回振ったとき、出た目の合計が B になることはありますか？
    # 1,2,...,6 の出目がある 6 面サイコロを A 回振ったとき、出た目の合計が B になることはありますか？
    # 1,2,...,6 の出目がある 6 面サイコロを A 回振ったとき、出た目の合計が B になることはありますか？
    # 1,2,...,6 の出目がある 6 面サイコロを A 回

=======
Suggestion 7

def main():
    # A, B = map(int, input().split())
    A, B = 2, 11

    # 1,2,...,6 の出目がある 6 面サイコロを A 回振ったとき、出た目の合計が B になることはありますか？
    # 6 ** A 通りの出目の組み合わせを全部試す
    # 6 ** A 通り試すのは無理なので、A 回振ったときに出る出目の和の最小値と最大値を求める
    # 最小値は A * 1、最大値は A * 6
    # 最小値が B より大きい場合は No
    # 最大値が B より小さい場合は No
    # 最小値と最大値の間に B があれば Yes
    # どれにも当てはまらない場合は No

    # 最小値
    min_sum = A * 1
    # 最大値
    max_sum = A * 6

    if B < min_sum or max_sum < B:
        print('No')
    else:
        print('Yes')

=======
Suggestion 8

def main():
    A, B = map(int, input().split())
    if A > 100 or B > 1000:
        print('Error')
        return
    if A < 1 or B < 1:
        print('Error')
        return
    if A * 6 < B:
        print('No')
        return
    print('Yes')

=======
Suggestion 9

def main():
    # A と B の入力
    A, B = map(int, input().split())
    # Yes / No の出力
    print("Yes" if (1 <= A and A <= 100) and (1 <= B and B <= 1000) and (A * 1 <= B and B <= A * 6) else "No")
