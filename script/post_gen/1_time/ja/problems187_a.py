Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    S_A = sum(map(int, list(str(A))))
    S_B = sum(map(int, list(str(B))))
    print(max(S_A, S_B))

main()

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    S_A = sum(int(i) for i in str(A))
    S_B = sum(int(i) for i in str(B))
    print(max(S_A, S_B))

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    S_A = sum(map(int, str(A)))
    S_B = sum(map(int, str(B)))
    print(max(S_A, S_B))

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if sum(map(int, list(str(a)))) > sum(map(int, list(str(b)))): print(sum(map(int, list(str(a)))))
    else: print(sum(map(int, list(str(b)))))

=======
Suggestion 5

def sum_digit(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print(max(sum(map(int, str(a))), sum(map(int, str(b)))))

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    a = sum(map(int, str(a)))
    b = sum(map(int, str(b)))
    print(max(a, b))

=======
Suggestion 8

def main():
    A, B = map(int, input().split())
    A = list(str(A))
    B = list(str(B))
    A_sum = 0
    B_sum = 0
    for i in A:
        A_sum += int(i)
    for i in B:
        B_sum += int(i)
    if A_sum > B_sum:
        print(A_sum)
    else:
        print(B_sum)

=======
Suggestion 9

def main():
    a,b = map(int,input().split())
    print(max(sum(list(map(int,list(str(a))))),sum(list(map(int,list(str(b)))))))

=======
Suggestion 10

def main():
    #入力
    A, B = map(int, input().split())
    #S(A)を求める
    S_A = 0
    while A > 0:
        S_A += A % 10
        A //= 10
    #S(B)を求める
    S_B = 0
    while B > 0:
        S_B += B % 10
        B //= 10
    #S(A)とS(B)のうち大きい方を出力
    if S_A > S_B:
        print(S_A)
    else:
        print(S_B)
