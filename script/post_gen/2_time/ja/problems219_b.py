Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    ans = ""
    for i in T:
        if i == "1":
            ans += S1
        elif i == "2":
            ans += S2
        else:
            ans += S3
    print(ans)

=======
Suggestion 2

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    ans = ""
    for i in range(len(T)):
        if T[i] == "1":
            ans += S1
        elif T[i] == "2":
            ans += S2
        elif T[i] == "3":
            ans += S3
    print(ans)

=======
Suggestion 3

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    ans = ''
    for i in T:
        if i == '1':
            ans += S1
        elif i == '2':
            ans += S2
        else:
            ans += S3
    print(ans)

=======
Suggestion 4

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    for i in T:
        if i == '1':
            print(S1, end="")
        elif i == '2':
            print(S2, end="")
        elif i == '3':
            print(S3, end="")

=======
Suggestion 5

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    S = [S1, S2, S3]
    for i in T:
        print(S[int(i)-1], end="")

=======
Suggestion 6

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    S = [S1, S2, S3]
    ans = ""
    for i in range(len(T)):
        ans += S[int(T[i]) - 1]
    print(ans)

=======
Suggestion 7

def main():
    S = [input() for _ in range(3)]
    T = input()
    ans = ""
    for t in T:
        ans += S[int(t)-1]
    print(ans)

=======
Suggestion 8

def main():
    #入力
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    #出力
    for i in range(len(T)):
        if T[i] == '1':
            print(S1, end='')
        elif T[i] == '2':
            print(S2, end='')
        elif T[i] == '3':
            print(S3, end='')
        else:
            print('error')
            break

=======
Suggestion 9

def main():
    S = [input() for _ in range(3)]
    T = input()
    for c in T:
        print(S[int(c)-1], end='')
    print()
