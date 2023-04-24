Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 0:
            if str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]:
                count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 0:
            if str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]:
                ans += 1
    print(ans)

=======
Suggestion 3

def solve(n):
    return len([i for i in range(1, n+1) if len(str(i)) % 2 == 0 and str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]])

=======
Suggestion 4

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 0:
            if str(i)[:int(len(str(i))/2)] == str(i)[int(len(str(i))/2):]:
                count += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 0 and str(i)[:int(len(str(i))/2)] == str(i)[int(len(str(i))/2):]:
            count += 1
    print(count)

=======
Suggestion 6

def solve():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if len(str(i)) % 2 == 0:
            if str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]:
                count += 1
    return count

print(solve())

=======
Suggestion 7

def main():
    n = int(input())
    result = 0
    for i in range(1, n + 1):
        if len(str(i)) % 2 == 0:
            if str(i)[:len(str(i)) // 2] == str(i)[len(str(i)) // 2:]:
                result += 1
    print(result)

=======
Suggestion 8

def main():
    N = int(input())
    N_str = str(N)
    N_len = len(N_str)
    N_half = N_len // 2
    count = 0
    for i in range(1, N+1):
        i_str = str(i)
        i_len = len(i_str)
        if i_len % 2 == 0:
            if i_str[:N_half] == i_str[N_half:]:
                count += 1
    print(count)

=======
Suggestion 9

def main():
    # Take input Here and Call solution function
    N = int(input())
    print(solution(N))

=======
Suggestion 10

def count(n):
    s = str(n)
    l = len(s)
    if l % 2 == 1:
        return 0
    else:
        l2 = l // 2
        s1 = s[:l2]
        s2 = s[l2:]
        if s1 == s2:
            return 1
        else:
            return 0
