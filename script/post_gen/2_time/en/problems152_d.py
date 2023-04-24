Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if str(i)[-1] == str(j)[0]:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if str(i)[0] == str(j)[-1] and str(i)[-1] == str(j)[0]:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    cnt = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if str(i)[-1] == str(j)[0] and str(i)[0] == str(j)[-1]:
                cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    N = int(input())
    cnt = [0] * 10
    for i in range(1, N + 1):
        cnt[i % 10] += 1
    ans = 0
    for i in range(1, N + 1):
        ans += cnt[i // 10 % 10] * cnt[i % 10]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        ans += 9 * (i // 10) + (i % 10)
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    if N == 1:
        print(1)
        return
    counter = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if str(i)[-1] == str(j)[0] and str(i)[0] == str(j)[-1]:
                counter += 1
    print(counter)

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        ans += N // 10 ** len(str(i))
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    # 1桁の数の数は10
    # 10桁の数の数は9*9=81
    # 100桁の数の数は9*9*9=729
    # 1000桁の数の数は9*9*9*9=6561
    # 10000桁の数の数は9*9*9*9*9=59049
    # 100000桁の数の数は9*9*9*9*9*9=531441
    # 1000000桁の数の数は9*9*9*9*9*9*9=4782969
    # 10000000桁の数の数は9*9*9*9*9*9*9*9=43046721
    # 100000000桁の数の数は9*9*9*9*9*9*9*9*9=387420489
    # 1000000000桁の数の数は9*9*9*9*9*9*9*9*9*9=3486784401
    # 10000000000桁の数の数は9*9*9*9*9*9*9*9*9*9*9=31381059609
    # 100000000000桁の数の数は9*9*9*9*9*9*9*9*9*9*9*9=282429536481
    # 1000000000000桁の数の数は9*9*9*9*9*9*9*9*9*9*9*9*9=2541865828329
    # 10000000000000桁の数の数は9*9*9*9*9*9*9*9*9*9*9*9*9*9=22876792454961
    # 100000000000000桁の数の数は9*9*9*9*9*9*9*9*9*9*9*9*9*9*9=205891132094649
