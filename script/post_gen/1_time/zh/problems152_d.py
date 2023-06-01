Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i % 10 == int(j / 10) and i / 10 == j % 10:
                count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i % 10 == 0:
            continue
        for j in range(1, N+1):
            if j % 10 == 0:
                continue
            if str(i)[0] == str(j)[-1] and str(i)[-1] == str(j)[0]:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        for j in range(i, N+1):
            if i%10 == j//100 and j%10 == i//100:
                cnt += 2
                if i == j:
                    cnt -= 1
    print(cnt)

=======
Suggestion 4

def main():
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if str(i)[-1] == str(j)[0] and str(i)[0] == str(j)[-1]:
                cnt += 1
    print(cnt)

=======
Suggestion 5

def get_num(n):
    num = 0
    for i in range(1,n+1):
        if i < 10:
            num += 1
        else:
            if i % 10 == i // (10 ** (len(str(i)) - 1)):
                num += 1
    return num

=======
Suggestion 6

def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        s = str(i)
        if s[0] == s[-1]:
            ans += 1
    print(ans)

=======
Suggestion 7

def get_num(n):
    count = 0
    for i in range(1,n+1):
        if i < 10:
            count += 1
            continue
        if i % 10 == int(str(i)[0]):
            count += 1
    return count

=======
Suggestion 8

def main():
    n = int(input())
    print(solve(n))

=======
Suggestion 9

def f(n):
    ans = 0
    for i in range(1, n+1):
        s = str(i)
        if s[0] == s[-1]:
            ans += 1
    return ans

=======
Suggestion 10

def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        if i%10 == 0:
            continue
        else:
            str_i = str(i)
            len_i = len(str_i)
            if str_i[-1] == str_i[0]:
                count += 1
            else:
                if len_i == 1:
                    continue
                else:
                    for j in range(1,len_i):
                        if str_i[j] == str_i[j-1]:
                            count += 1
                            break
    print(count)
main()
