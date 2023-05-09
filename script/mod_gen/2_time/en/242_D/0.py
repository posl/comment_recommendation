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

if __name__ == '__main__':
    main()