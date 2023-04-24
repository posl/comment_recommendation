Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    cnt = 0
    for i in range(N):
        if S[i] == "R":
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i - 1] += (cnt + 1) // 2
            cnt = 0
    print(*ans)

=======
Suggestion 2

def main():
    s = input()
    n = len(s)
    l = [0] * n
    r = [0] * n
    for i in range(n):
        if s[i] == 'L':
            l[i] = 1
        else:
            r[i] = 1
    for i in range(n):
        if i > 0:
            l[i] += l[i-1]
        if i < n-1:
            r[n-1-i] += r[n-i]
    for i in range(n):
        print(l[i] + r[i], end=' ')

=======
Suggestion 3

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    ans[0] = 1
    ans[N-1] = 1
    for i in range(N-1):
        if S[i] == 'R' and S[i+1] == 'L':
            cnt = 1
            for j in range(i+1,N):
                if S[j] == 'L':
                    cnt += 1
                else:
                    break
            if cnt % 2 == 1:
                ans[i] += cnt // 2 + 1
                ans[i+1] += cnt // 2
            else:
                ans[i] += cnt // 2
                ans[i+1] += cnt // 2
        elif S[i] == 'L' and S[i+1] == 'R':
            cnt = 1
            for j in range(i-1,-1,-1):
                if S[j] == 'R':
                    cnt += 1
                else:
                    break
            if cnt % 2 == 1:
                ans[i] += cnt // 2 + 1
                ans[i+1] += cnt // 2
            else:
                ans[i] += cnt // 2
                ans[i+1] += cnt // 2
    print(*ans)

=======
Suggestion 4

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    ans[0] = 1
    ans[N-1] = 1
    for i in range(1, N):
        if S[i] == 'R' and S[i-1] == 'L':
            ans[i] += ans[i-1]
            ans[i-1] = 0
        else:
            ans[i] += ans[i-1]
    for i in range(N-1, 0, -1):
        if S[i] == 'L' and S[i-1] == 'R':
            ans[i-1] += ans[i]
            ans[i] = 0
        else:
            ans[i-1] += ans[i]
    print(*ans)

=======
Suggestion 5

def main():
    s = input()
    n = len(s)
    ans = [0] * n
    for i in range(n):
        if s[i] == 'R':
            ans[i+1] += 1
        else:
            ans[i-1] += 1
    for i in range(n):
        print(ans[i]//2, end=' ')
    print()

=======
Suggestion 6

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    ans[0] = 1
    ans[-1] = 1
    for i in range(1, N-1):
        if S[i] == "R":
            ans[i] += ans[i-1] + 1
        else:
            ans[i] += ans[i+1] + 1
    print(*ans)

=======
Suggestion 7

def main():
    s = input()
    n = len(s)
    cnt = 0
    ans = [0] * n
    for i in range(n):
        if s[i] == 'L':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i - 1] += (cnt + 1) // 2
            cnt = 0
    print(*ans)

=======
Suggestion 8

def main():
    S = input()

    N = len(S)
    X = [0] * N
    X[0] = 1
    X[-1] = 1

    for i in range(1, N - 1):
        if S[i - 1] == S[i]:
            X[i] = X[i - 1] + 1
        else:
            X[i] = 1

    for i in range(N - 2, 0, -1):
        if S[i - 1] == S[i]:
            X[i] = X[i + 1] + 1

    print(*X)

=======
Suggestion 9

def main():
    S = input()

    N = len(S)
    people = [1] * N
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            people[i] += people[i + 1]
            people[i + 1] = 0

    for i in range(N - 1, 0, -1):
        if S[i - 1] == S[i]:
            people[i] += people[i - 1]
            people[i - 1] = 0

    print(*people)

=======
Suggestion 10

def main():
    S = input()
    N = len(S)
    # N = 10**5
    # S = "R" * (N-1) + "L"
    # S = "RRLRL"
    # S = "RRLLLLRLRRLL"
    # S = "RRRLLRLLRRRLLLLL"
    # print(S)

    # 連続するRの数を数える
    # Lが来たら、左から順に1ずつ足していく
    # 連続するRの数が奇数なら、中央のマスには2人、それ以外には1人
    # 連続するRの数が偶数なら、全て1人
    # Rが来たら、右から順に1ずつ足していく
    # 連続するLの数が奇数なら、中央のマスには2人、それ以外には1人
    # 連続するLの数が偶数なら、全て1人

    # 連続するRの数を数える
    count = 0
    for i in range(N):
        if S[i] == "R":
            count += 1
        else:
            break

    # 連続するRの数が奇数なら、中央のマスには2人、それ以外には1人
    if count % 2 == 1:
        ans = [1] * (count // 2) + [2] + [1] * (count // 2)
    # 連続するRの数が偶数なら、全て1人
    else:
        ans = [1] * count

    # Rが来たら、右から順に1ずつ足していく
    for i in range(N-1, count-1, -1):
        if S[i] == "L":
            ans[i-count] += 1
        else:
            break

    # 連続するLの数を数える
    count = 0
    for i
