Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = [input() for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if S[i][j] == ".":
                S[i] = S[i][:j] + "#" + S[i][j+1:]
                if check(S):
                    print("Yes")
                    return
                S[i] = S[i][:j] + "." + S[i][j+1:]
    print("No")

=======
Suggestion 2

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
Suggestion 3

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 'No'
    for i in range(N):
        for j in range(N):
            if S[i][j] == '.':
                S[i] = S[i][:j] + '#' + S[i][j+1:]
                for k in range(N):
                    for l in range(N):
                        if S[k][l] == '.':
                            S[k] = S[k][:l] + '#' + S[k][l+1:]
                            for m i

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for i in range(N)]
    ans = "No"
    for i in range(N):
        for j in range(N):
            if S[i][j] == ".":
                S[i] = S[i][:j] + "#" + S[i][j+1:]
                for k in range(N):
                    for l in range(N):
                        if S[k][l] == ".":
                            S[k] = S[k][:l] + "#" + S[k][l+1:]
                            for m in range(N):
                                for n in range(N):
                                    if S[m][n] == "#":
                                        if m+5 < N:
                                            if S[m+1][n] == "#" and S[m+2][n] == "#" and S[m+3][n] == "#" and S[m+4][n] == "#" and S[m+5][n] == "#":
                                                ans = "Yes"
                                        if n+5 < N:
                                            if S[m][n+1] == "#" and S[m][n+2] == "#" and S[m][n+3] == "#" and S[m][n+4] == "#" and S[m][n+5] == "#":
                                                ans = "Yes"
                                        if m+5 < N and n+5 < N:
                                            if S[m+1][n+1] == "#" and S[m+2][n+2] == "#" and S[m+3][n+3] == "#" and S[m+4][n+4] == "#" and S[m+5][n+5] == "#":
                                                ans = "Yes"
                                        if m+5 < N and n-5 >= 0:
                                            if S[m+1][n-1] == "#" and S[m+2][n-2] == "#" and S[m+3][n-3] == "#" and S[m+4][n-4] == "#" and S[m+5][n-5] == "#":
                                                ans = "Yes"
                            S[k] = S[k][:l] + "." + S[k][l+1:]
                S[i] = S[i][:j] + "." + S[i][j+1:]
    print(ans)

=======
Suggestion 5

def solve():
    N = int(input())
    S = [input() for _ in range(N)]
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
Suggestion 6

def main():
    n = int(input())
    s = [input() for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if s[i][j] == "#":
                continue
            s[i] = s[i][:j] + "#" + s[i][j+1:]
            if check(s):
                print("Yes")
                return
            s[i] = s[i][:j] + "." + s[i][j+1:]
            for k in range(i, n):
                for l in range(n):
                    if s[k][l] == "#":
                        continue
                    s[k] = s[k][:l] + "#" + s[k][l+1:]
                    if check(s):
                        print("Yes")
                        return
                    s[k] = s[k][:l] + "." + s[k][l+1:]

    print("No")

=======
Suggestion 7

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == "#":
                continue
            for d in range(4):
                cnt = 1
                for k in range(1, 6):
                    ni = i + k * dx[d]
                    nj = j + k * dy[d]
                    if ni < 0 or ni >= N or nj < 0 or nj >= N:
                        break
                    if S[ni][nj] == "#":
                        cnt += 1
                    else:
                        break
                if cnt == 6:
                    print("Yes")
                    return
    print("No")

=======
Suggestion 8

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N-5):
        for j in range(N-5):
            # 横方向
            if S[i][j:j+6] == "######":
                print("Yes")
                return
            # 縦方向
            if all(S[i+k][j] == "#" for k in range(6)):
                print("Yes")
                return
            # 右下方向
            if all(S[i+k][j+k] == "#" for k in range(6)):
                print("Yes")
                return
            # 左下方向
            if all(S[i+k][j-k] == "#" for k in range(6)):
                print("Yes")
                return
    print("No")

=======
Suggestion 9

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print("Yes" if check(N, S) else "No")

=======
Suggestion 10

def main():
    N = int(input())
    S = [input() for _ in range(N)]

    #縦方向に黒く塗られたマスが6つ以上連続するか判定
    for i in range(N):
        for j in range(N-5):
            if S[i][j] == '#' and S[i][j+1] == '#' and S[i][j+2] == '#' and S[i][j+3] == '#' and S[i][j+4] == '#' and S[i][j+5] == '#':
                print('Yes')
                return
    #横方向に黒く塗られたマスが6つ以上連続するか判定
    for i in range(N-5):
        for j in range(N):
            if S[i][j] == '#' and S[i+1][j] == '#' and S[i+2][j] == '#' and S[i+3][j] == '#' and S[i+4][j] == '#' and S[i+5][j] == '#':
                print('Yes')
                return
    #右下方向に黒く塗られたマスが6つ以上連続するか判定
    for i in range(N-5):
        for j in range(N-5):
            if S[i][j] == '#' and S[i+1][j+1] == '#' and S[i+2][j+2] == '#' and S[i+3][j+3] == '#' and S[i+4][j+4] == '#' and S[i+5][j+5] == '#':
                print('Yes')
                return
    #左下方向に黒く塗られたマスが6つ以上連続するか判定
    for i in range(5,N):
        for j in range(N-5):
            if S[i][j] == '#' and S[i-1][j+1] == '#' and S[i-2][j+2] == '#' and S[i-3][j+3] == '#' and S[i-4][j+4] == '#' and S[i-5][j+5] == '#':
                print('Yes')
