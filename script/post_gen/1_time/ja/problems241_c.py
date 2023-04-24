Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        for j in range(N):
            if S[i][j] == ".":
                S[i] = S[i][:j] + "#" + S[i][j+1:]
                if check(S):
                    print("Yes")
                    return
                for k in range(N):
                    for l in range(N):
                        if S[k][l] == ".":
                            S[k] = S[k][:l] + "#" + S[k][l+1:]
                            if check(S):
                                print("Yes")
                                return
                            S[k] = S[k][:l] + "." + S[k][l+1:]
                S[i] = S[i][:j] + "." + S[i][j+1:]
    print("No")

=======
Suggestion 2

def main():
    N = int(input())
    S = [input() for i in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == ".":
                S[i] = S[i][:j] + "#" + S[i][j + 1:]
                if six(S):
                    print("Yes")
                    return
                for k in range(N):
                    for l in range(N):
                        if S[k][l] == ".":
                            S[k] = S[k][:l] + "#" + S[k][l + 1:]
                            if six(S):
                                print("Yes")
                                return
                            S[k] = S[k][:l] + "." + S[k][l + 1:]
                S[i] = S[i][:j] + "." + S[i][j + 1:]
    print("No")

=======
Suggestion 3

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == ".":
                S[i][j] = "#"
                if check(S, N):
                    print("Yes")
                    return
                S[i][j] = "."
    print("No")

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for i in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == "#":
                continue
            S[i] = S[i][:j] + "#" + S[i][j+1:]
            for k in range(N):
                if S[k][j] == "#":
                    continue
                S[k] = S[k][:j] + "#" + S[k][j+1:]
                if is_satisfied(S, N):
                    print("Yes")
                    return
                S[k] = S[k][:j] + "." + S[k][j+1:]
            S[i] = S[i][:j] + "." + S[i][j+1:]
    print("No")

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for i in range(N)]
    #N = 6
    #S = ["#######", "#######", "#######", "#######", "#######", "#######"]
    #N = 10
    #S = ["..........", "##..##.....", "..........", "..........", "....#.....", "....#.....", "#.#...#..#.", "..........", "..........", ".........."]
    #N = 8
    #S = ["........", "........", ".#.##.#.", "........", "........", "........", "........", "........"]
    #N = 6
    #S = ["#.....#", "##...##", "##.#.##", ".#.#.#.", "..###..", "......."]
    #N = 6
    #S = [".......", "..###..", ".#.#.#.", "##.#.##", "##...##", "#.....#"]
    #N = 6
    #S = ["#.....#", "..###..", ".#.#.#.", "##.#.##", "##...##", "#.....#"]
    #N = 6
    #S = ["#.....#", "##...##", "##.#.##", ".#.#.#.", "..###..", "#.....#"]
    #N = 6
    #S = ["#.....#", "..###..", ".#.#.#.", "##.#.##", "##...##", "......."]
    #N = 6
    #S = [".......", "##...##", "##.#.##", ".#.#.#.", "..###..", "#.....#"]
    #N = 6
    #S = ["#.....#", "##...##", "##.#.##", ".#.#.#.", "..###..", "......."]
    #N = 6
    #S = [".......", "..###..", ".#.#.#.", "##.#.##", "##...##", "#.....#"]
    #N = 6
    #S = ["#.....#", "..###..", ".#.#.#.", "##.#.##", "##...##", "......."]
    #N = 6
    #S = ["

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for _ in range(N)]

    for i in range(N-5):
        for j in range(N-5):
            if S[i][j] == '.':
                S[i] = S[i][:j] + '#' + S[i][j+1:]
                for k in range(6):
                    if S[i+k][j] == '.':
                        S[i+k] = S[i+k][:j] + '#' + S[i+k][j+1:]
                    if S[i][j+k] == '.':
                        S[i] = S[i][:j+k] + '#' + S[i][j+k+1:]
                    if S[i+k][j+k] == '.':
                        S[i+k] = S[i+k][:j+k] + '#' + S[i+k][j+k+1:]
                    if S[i+k][j+5-k] == '.':
                        S[i+k] = S[i+k][:j+5-k] + '#' + S[i+k][j+5-k+1:]
                for k in range(6):
                    if S[i+k][j] == '.':
                        S[i+k] = S[i+k][:j] + '#' + S[i+k][j+1:]
                    if S[i][j+k] == '.':
                        S[i] = S[i][:j+k] + '#' + S[i][j+k+1:]
                    if S[i+k][j+k] == '.':
                        S[i+k] = S[i+k][:j+k] + '#' + S[i+k][j+k+1:]
                    if S[i+k][j+5-k] == '.':
                        S[i+k] = S[i+k][:j+5-k] + '#' + S[i+k][j+5-k+1:]
                for k in range(6):
                    if S[i+k][j] == '.':
                        S[i+k] = S[i+k][:j] + '#' + S[i+k][j+1:]
                    if S[i][j+k] == '.':
                        S[i] = S[i][:j+k] + '#' + S[i][j+k+1:]
                    if S[i+k][j+k] == '.':
                        S[i+k] = S[i+k][:j+k] + '#' + S[i+k][j+k+1:]
                    if S[i+k][j+5-k

=======
Suggestion 7

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    # print(N)
    # print(S)
    for i in range(N-5):
        for j in range(N-5):
            if S[i][j] == ".":
                if S[i][j+1] == "." and S[i][j+2] == "." and S[i][j+3] == "." and S[i][j+4] == "." and S[i][j+5] == ".":
                    print("Yes")
                    return
                if S[i+1][j] == "." and S[i+2][j] == "." and S[i+3][j] == "." and S[i+4][j] == "." and S[i+5][j] == ".":
                    print("Yes")
                    return
                if S[i+1][j+1] == "." and S[i+2][j+2] == "." and S[i+3][j+3] == "." and S[i+4][j+4] == "." and S[i+5][j+5] == ".":
                    print("Yes")
                    return
                if S[i+1][j-1] == "." and S[i+2][j-2] == "." and S[i+3][j-3] == "." and S[i+4][j-4] == "." and S[i+5][j-5] == ".":
                    print("Yes")
                    return
    print("No")

=======
Suggestion 8

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    #print(N)
    #print(S)

    # 横方向
    for i in range(N):
        cnt = 0
        for j in range(N):
            if S[i][j] == '#':
                cnt = 0
            else:
                cnt += 1
                if cnt >= 6:
                    print('Yes')
                    exit()
    # 縦方向
    for j in range(N):
        cnt = 0
        for i in range(N):
            if S[i][j] == '#':
                cnt = 0
            else:
                cnt += 1
                if cnt >= 6:
                    print('Yes')
                    exit()
    # 斜め方向
    for i in range(N):
        cnt = 0
        for j in range(N):
            if i + j >= N:
                break
            if S[i+j][j] == '#':
                cnt = 0
            else:
                cnt += 1
                if cnt >= 6:
                    print('Yes')
                    exit()

    for i in range(N):
        cnt = 0
        for j in range(N):
            if i + j >= N:
                break
            if S[j][i+j] == '#':
                cnt = 0
            else:
                cnt += 1
                if cnt >= 6:
                    print('Yes')
                    exit()

    for i in range(N):
        cnt = 0
        for j in range(N):
            if i - j < 0:
                break
            if S[i-j][j] == '#':
                cnt = 0
            else:
                cnt += 1
                if cnt >= 6:
                    print('Yes')
                    exit()

    for i in range(N):
        cnt = 0
        for j in range(N):
            if i - j < 0:
                break
            if S[j][i-j] == '#':
                cnt = 0
            else:
                cnt += 1
                if cnt >= 6:
                    print('Yes')
                    exit()

    print('No')

=======
Suggestion 9

def main():
    N = int(input())
    S = [input() for i in range(N)]

    # 連続する黒のマスの数を数える
    def count_black(i, j, di, dj):
        count = 0
        while 0 <= i < N and 0 <= j < N:
            if S[i][j] == '#':
                count += 1
            else:
                break
            i += di
            j += dj
        return count

    # すべてのマスについて、8方向について黒のマスが6個以上連続しているかどうかをチェック
    for i in range(N):
        for j in range(N):
            if S[i][j] == '.':
                continue
            for di, dj in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                if count_black(i, j, di, dj) + count_black(i, j, -di, -dj) >= 7:
                    print('Yes')
                    return
    print('No')

=======
Suggestion 10

def main():
    N = int(input())
    S = [input() for _ in range(N)]

    # 6連続の黒マスが存在するか判定する
    def is_6consecutive_black():
        for i in range(N-5):
            for j in range(N-5):
                # 6行6列のマス目を取得
                S_ = [S[k][j:j+6] for k in range(i, i+6)]
                # 一つでも黒マスがなければNG
                if '#' not in ''.join(S_):
                    continue
                # 対角線上のマスがすべて黒マスであればOK
                if all(S_[k][k] == '#' for k in range(6)):
                    return True
        return False

    # 白マスの数を数える
    cnt = sum(s.count('.') for s in S)
    if cnt == 0:
        # 白マスがなければOK
        print('Yes')
    elif cnt == 1:
        # 白マスが1つならば、そのマスを黒く塗ればOK
        print('Yes')
    else:
        # 白マスが2つ以上あれば、2つのマスを黒く塗ればOK
        print('Yes' if is_6consecutive_black() else 'No')

main()
