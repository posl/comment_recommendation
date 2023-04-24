Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if S[i] != S[j] and S[i] != S[k] and S[j] != S[k] and j-i != k-j:
                    ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if S[i] != S[j] and S[j] != S[k] and S[k] != S[i] and j-i != k-j:
                    ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if S[i] != S[j] and S[i] != S[k] and S[j] != S[k] and j-i != k-j:
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if s[i] != s[j] and s[i] != s[k] and s[j] != s[k] and j-i != k-j:
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                    if j - i != k - j:
                        ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if s[i] != s[j] and s[j] != s[k] and s[i] != s[k]:
                    if j - i != k - j:
                        cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    cnt = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if s[i] != s[j] and s[i] != s[k] and s[j] != s[k] and j-i != k-j:
                    cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    rgb = [0, 0, 0]
    for c in S:
        if c == "R":
            rgb[0] += 1
        elif c == "G":
            rgb[1] += 1
        elif c == "B":
            rgb[2] += 1
    ans = rgb[0] * rgb[1] * rgb[2]
    for i in range(N):
        for j in range(i + 1, N):
            k = j + (j - i)
            if k >= N:
                break
            if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                ans -= 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    S = input()

    # 1文字目と2文字目が異なる場合、3通り
    # 1文字目と3文字目が異なる場合、3通り
    # 2文字目と3文字目が異なる場合、3通り
    # 1文字目と2文字目が異なる場合、3通り
    # 1文字目と3文字目が異なる場合、3通り
    # 2文字目と3文字目が異なる場合、3通り
    # 1文字目と2文字目が異なる場合、3通り
    # 1文字目と3文字目が異なる場合、3通り
    # 2文字目と3文字目が異なる場合、3通り
    # 1文字目と2文字目が異なる場合、3通り
    # 1文字目と3文字目が異なる場合、3通り
    # 2文字目と3文字目が異なる場合、3通り
    # 1文字目と2文字目が異なる場合、3通り
    # 1文字目と3文字目が異なる場合、3通り
    # 2文字目と3文字目が異なる場合、3通り
    # 1文字目と2文字目が異なる場合、3通り
    # 1文字目と3文字目が異なる場合、3通り
    # 2文字目と3文字目が異なる場合、3通り
    # 1文字目と2文字目が異なる場合、3通り
    # 1文字目と3文字目が異なる場合、3通り
    # 2文字目と3文字目が異なる場合、3通り
    # 1文字目と2文字目が異なる場合、3通り
    #
