Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    #input()函数返回的是str类型，所以要转换成int类型
    N = int(input())
    S = input().split()
    #map()函数接收两个参数，一个是函数，一个是Iterable，
    #map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
    S = list(map(int,S))
    return N,S

=======
Suggestion 2

def get_area(a, b):
    return 4*a*b + 3*a + 3*b

N = int(input())
S = list(map(int, input().split()))

count = 0
for i in range(N):
    for j in range(i+1, N):
        if S[i] == S[j]:
            continue
        for a in range(1, 1000):
            for b in range(1, 1000):
                if S[i] == get_area(a, b) and S[j] == get_area(a, b):
                    count += 1
print(count)

=======
Suggestion 3

def main():
    n = int(input())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(0, n):
        a = 1
        while a * a <= s[i]:
            if s[i] % a == 0:
                b = s[i] // a
                if 4 * a * b + 3 * a + 3 * b == s[i]:
                    break
            a += 1
        if a * a > s[i]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    #输入
    N = int(input())
    S = list(map(int,input().split()))

    #计算
    count = 0
    for i in range(N):
        # 4ab+3a+3b = S_i
        # 4ab+3a+3b-S_i = 0
        # (4b+3)a+(4a+3)b-S_i = 0
        # (4b+3)a = (S_i-(4a+3)b)
        # a = (S_i-(4a+3)b)/(4b+3)
        # b = (S_i-(4b+3)a)/(4a+3)
        # a = (S_i-(4a+3)((S_i-(4b+3)a)/(4a+3)))/(4((S_i-(4b+3)a)/(4a+3))+3)
        # a = (S_i-(4a+3)((S_i-(4b+3)a)/(4a+3)))/(S_i-(4b+3)a+3)
        # a = (S_i-(4a+3)(S_i-(4b+3)a)/(4a+3))/(S_i-(4b+3)a+3)
        # a = (S_i-(4a+3)(S_i-(4b+3)a)/(4a+3))/(S_i-(4b+3)a+3)
        # a = (S_i-(4a+3)(S_i-(4b+3)a)/(4a+3))/(S_i-(4b+3)a+3)
        # a = (S_i-(4a+3)(S_i-(4b+3)a)/(4a+3))/(S_i-(4b+3)a+3)
        # a = (S_i-(4a+3)(S_i-(4b+3)a)/(4a+3))/(S_i-(4b+3)a+3)
        # a = (S_i-(4a+3)(S_i-(4b+3)a)/(4a+3))/(S_i-(4b+3)a+3)
        # a = (S_i-(4a+3)(S_i-(4b+3)a)/(4a+3))/(S_i-(4b+3)a+3)

=======
Suggestion 5

def get_input():
    N = int(input())
    S = [int(i) for i in input().split()]
    return N, S

=======
Suggestion 6

def main():
    n = int(input())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    s = list(map(int,input().split()))
    result = 0
    for i in range(n):
        for j in range(i+1,n):
            if s[i] == s[j]:
                result += 1
    print(result)

=======
Suggestion 8

def main():
    n = int(input())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if s[i] % 2 == 0:
            ans += 1
        elif s[i] % 3 == 0:
            ans += 1
        elif s[i] % 5 == 0:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    for i in range(n):
        a = 1
        while a * a <= s[i]:
            if s[i] % a == 0:
                b = s[i] // a
                if 4 * a * b + 3 * a + 3 * b == s[i]:
                    break
            a += 1
        if a * a > s[i]:
            count += 1
    print(count)

=======
Suggestion 10

def problems227_b(N):
    S = []
    for i in range(N):
        S.append(int(input()))
    count = 0
    for i in range(N):
        a = 1
        while a * a <= S[i]:
            if S[i] % a == 0:
                b = S[i] // a
                if 4 * a * b + 3 * a + 3 * b == S[i]:
                    break
            a += 1
        if a * a > S[i]:
            count += 1
    print(count)
