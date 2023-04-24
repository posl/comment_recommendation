Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    ans = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if sorted(S[i]) == sorted(S[j]):
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if S[i] == S[j]:
                continue
            if len(S[i]) != len(S[j]):
                break
            if sorted(S[i]) == sorted(S[j]):
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S = [input() for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if sorted(S[i]) == sorted(S[j]):
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if sorted(S[i]) == sorted(S[j]):
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()

    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if S[i] == S[j]:
                continue
            if sorted(S[i]) == sorted(S[j]):
                ans += 1
    print(ans)

=======
Suggestion 6

def get_anagram_count(s_list):
    s_dict = {}
    count = 0
    for s in s_list:
        s_dict[s] = s_dict.get(s, 0) + 1
    for s in s_list:
        s_dict[s] -= 1
        for i in range(len(s)):
            s_dict[s[i + 1:] + s[:i + 1]] = s_dict.get(s[i + 1:] + s[:i + 1], 0) + 1
    for s in s_list:
        count += s_dict[s]
    return count

=======
Suggestion 7

def main():
    N = int(input())
    s = [input() for _ in range(N)]

    # s をソートしたものをリストに格納
    sort_s = ["".join(sorted(s[i])) for i in range(N)]

    # 重複を削除
    sort_s = list(set(sort_s))

    # 重複したものの個数をカウント
    count = [sort_s.count(sort_s[i]) for i in range(len(sort_s))]

    # 重複した文字列の個数の組み合わせをカウント
    ans = 0
    for i in range(len(count)):
        ans += count[i] * (count[i] - 1) // 2

    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    s = [input() for _ in range(N)]

    # sの文字列をソートして、辞書型にして、valueが2以上のものを数える
    ans = 0
    for i in range(N):
        s_dict = {}
        for j in range(N):
            if i != j:
                s_dict["".join(sorted(s[i]))] = s_dict.get("".join(sorted(s[i])), 0) + 1
        for v in s_dict.values():
            if v >= 2:
                ans += 1

    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    s = [input() for _ in range(N)]
    # s.sort()  # この場合、s.sort()を実行すると実行時間が長くなる
    # これは、s.sort()を実行すると、sの中身が並び替えられてしまうため。
    # なので、sの中身を並び替えずに、s.sort()の結果を別の変数に格納する。
    s_sort = sorted(s)
    # print(s)
    # print(s_sort)
    # print(s_sort[0])
    # print(s_sort[1])
    # print(s_sort[2])
    # print(s_sort[3])
    # print(s_sort[4])
    # print(s_sort[0][0])
    # print(s_sort[0][1])
    # print(s_sort[0][2])
    # print(s_sort[0][3])
    # print(s_sort[0][4])
    # print(s_sort[0][5])
    # print(s_sort[0][6])
    # print(s_sort[0][7])
    # print(s_sort[0][8])
    # print(s_sort[0][9])
    # print(s_sort[1][0])
    # print(s_sort[1][1])
    # print(s_sort[1][2])
    # print(s_sort[1][3])
    # print(s_sort[1][4])
    # print(s_sort[1][5])
    # print(s_sort[1][6])
    # print(s_sort[1][7])
    # print(s_sort[1][8])
    # print(s_sort[1][9])
    # print(s_sort[2][0])
    # print(s_sort[2][1])
    # print(s_sort[2][2])
    # print(s_sort[2][3])
    # print(s_sort[2][4])
    # print(s_sort[2][5])
    # print(s_sort[2][6])
    # print(s_sort[2][7])
    # print(s_sort[2][8])
    # print(s_sort[2][9])
    # print(s_sort[3][0])

=======
Suggestion 10

def anagramCount(strs):
    # strs: list of string
    # return: int
    # ここにプログラムを書く
    # ここまで

    return 0
