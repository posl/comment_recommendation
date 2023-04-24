Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    Q = int(input())
    T = []
    K = []
    for i in range(Q):
        t, k = map(int, input().split())
        T.append(t)
        K.append(k)
    for i in range(Q):
        t = T[i]
        k = K[i]
        if t == 0:
            print(S[k-1])
        else:
            if t % 3 == 1:
                if k % 3 == 1:
                    print('A')
                elif k % 3 == 2:
                    print('B')
                else:
                    print('C')
            elif t % 3 == 2:
                if k % 3 == 1:
                    print('B')
                elif k % 3 == 2:
                    print('C')
                else:
                    print('A')
            else:
                if k % 3 == 1:
                    print('C')
                elif k % 3 == 2:
                    print('A')
                else:
                    print('B')

main()

Problem Statement

You are given a string S consisting of A, B, C.

Let S^{(0)}:=S. For i=1,2,3,..., let S^{(i)} be the result of simultaneously replacing the characters of S^{(i-1)} as follows: A → BC, B → CA, C → AB.

Answer Q queries. The i-th query is as follows.

Print the k_i-th character from the beginning of S^{(t_i)}.

Constraints

S is a string of length between 1 and 10^5 (inclusive) consisting of A, B, C.

1 ≦ Q ≦ 10^5

0 ≦ t_i ≦ 10^{18}

1 ≦ k_i ≦ min(10^{18}, the length of S^{(t_i)})

Q, t_i, k_i are integers.

Input

Input is given from Standard Input in the following format:

S
Q
t_1 k_1
t_2 k_2
.
.
.
t_Q k_Q

Output

Process the Q queries in ascending order of index, that is, in the given order. Each answer should be followed by a newline.

Sample Input 1

ABC
4
0 1
1 1
1 3
1

=======
Suggestion 2

def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        if t % 3 == 0:
            if k % 3 == 1:
                print(S[0])
            elif k % 3 == 2:
                print(S[1])
            else:
                print(S[2])
        elif t % 3 == 1:
            if k % 3 == 1:
                print(S[1])
            elif k % 3 == 2:
                print(S[2])
            else:
                print(S[0])
        else:
            if k % 3 == 1:
                print(S[2])
            elif k % 3 == 2:
                print(S[0])
            else:
                print(S[1])

=======
Suggestion 3

def main():
    S = input()
    Q = int(input())
    for _ in range(Q):
        t, k = map(int, input().split())
        k -= 1
        for i in range(t, -1, -1):
            if S[k] == 'A':
                pass
            elif S[k] == 'B':
                if i % 3 == 1:
                    k = (k + 1) % len(S)
                elif i % 3 == 2:
                    k = (k - 1) % len(S)
            elif S[k] == 'C':
                if i % 3 == 1:
                    k = (k - 1) % len(S)
                elif i % 3 == 2:
                    k = (k + 1) % len(S)
        print(S[k])

=======
Suggestion 4

def main():
    S = input()
    Q = int(input())
    for _ in range(Q):
        t, k = map(int, input().split())
        t %= 3
        k -= 1
        if t == 0:
            print(S[k])
        elif t == 1:
            print(S[k + len(S) // 3])
        else:
            print(S[k + 2 * len(S) // 3])

=======
Suggestion 5

def main():
    S = input()
    Q = int(input())
    for _ in range(Q):
        t, k = map(int, input().split())
        print(solve(S, t, k))

=======
Suggestion 6

def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        print(S[(k - 1) % len(S)])

=======
Suggestion 7

def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        while t > 0:
            if S[k-1] == "A":
                if t % 3 == 1:
                    print("A")
                    break
                elif t % 3 == 2:
                    print("B")
                    break
                elif t % 3 == 0:
                    print("C")
                    break
            elif S[k-1] == "B":
                if t % 3 == 1:
                    print("B")
                    break
                elif t % 3 == 2:
                    print("C")
                    break
                elif t % 3 == 0:
                    print("A")
                    break
            elif S[k-1] == "C":
                if t % 3 == 1:
                    print("C")
                    break
                elif t % 3 == 2:
                    print("A")
                    break
                elif t % 3 == 0:
                    print("B")
                    break
            t -= 1

=======
Suggestion 8

def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        for j in range(t, -1, -1):
            if k > 2**j:
                k -= 2**j
                if S[j] == 'A':
                    S[j] = 'B'
                elif S[j] == 'B':
                    S[j] = 'C'
                elif S[j] == 'C':
                    S[j] = 'A'
        print(S[k-1])

=======
Suggestion 9

def main():
    S = input()
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    A = [0] * len(S)
    B = [0] * len(S)
    C = [0] * len(S)
    for i, s in enumerate(S):
        if s == 'A':
            A[i] = 1
        elif s == 'B':
            B[i] = 1
        else:
            C[i] = 1
    for i in range(1, len(S)):
        A[i] += A[i-1]
        B[i] += B[i-1]
        C[i] += C[i-1]
    for t, k in queries:
        if t % 3 == 0:
            print(S[k-1])
        elif t % 3 == 1:
            if A[k-1] > 0:
                print('A')
            elif B[k-1] > 0:
                print('B')
            else:
                print('C')
        else:
            if A[k-1] > B[k-1]:
                print('A')
            elif B[k-1] > C[k-1]:
                print('B')
            else:
                print('C')

=======
Suggestion 10

def main():
    S = input()
    Q = int(input())
    s = S
    for i in range(Q):
        t, k = map(int, input().split())
        if t == 0:
            s = s[k:] + s[:k]
        else:
            s = s[-k:] + s[:-k]
    print(s)
