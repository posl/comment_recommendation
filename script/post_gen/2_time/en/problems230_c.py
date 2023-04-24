Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (i + j) % 2 == (A + B) % 2:
                print('#', end='')
            else:
                print('.', end='')
        print()

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (max(1-A, 1-B) <= i-j <= min(N-A, N-B)) or (max(1-A, B-N) <= i+j-2*A <= min(N-A, B-1)):
                print("#", end="")
            else:
                print(".", end="")
        print("")

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (i + j) % 2 == (A + B) % 2:
                print("#", end="")
            else:
                print(".", end="")
        print()
main()

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if max(1-A, 1-B) <= i-j <= min(N-A, N-B):
                print('#', end='')
            elif max(1-A, B-N) <= i+j <= min(N-A, B-1):
                print('#', end='')
            else:
                print('.', end='')
        print()

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    #print(N, A, B)
    #print(P, Q, R, S)
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (i+j) % 2 == (A+B) % 2:
                print('#', end = '')
            else:
                print('.', end = '')
        print()

=======
Suggestion 6

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())

    #print(N, A, B)
    #print(P, Q, R, S)

    # 1 ≦ N ≦ 10^{18}
    # 1 ≦ A ≦ N
    # 1 ≦ B ≦ N
    # 1 ≦ P ≦ Q ≦ N
    # 1 ≦ R ≦ S ≦ N
    # (Q-P+1)×(S-R+1)≦ 3× 10^5
    # All values in input are integers.

    # 1 ≦ N ≦ 10^{18}
    # 1 ≦ A ≦ N
    # 1 ≦ B ≦ N
    # 1 ≦ P ≦ Q ≦ N
    # 1 ≦ R ≦ S ≦ N
    # (Q-P+1)×(S-R+1)≦ 3× 10^5
    # All values in input are integers.

    # 1 ≦ N ≦ 10^{18}
    # 1 ≦ A ≦ N
    # 1 ≦ B ≦ N
    # 1 ≦ P ≦ Q ≦ N
    # 1 ≦ R ≦ S ≦ N
    # (Q-P+1)×(S-R+1)≦ 3× 10^5
    # All values in input are integers.

    # 1 ≦ N ≦ 10^{18}
    # 1 ≦ A ≦ N
    # 1 ≦ B ≦ N
    # 1 ≦ P ≦ Q ≦ N
    # 1 ≦ R ≦ S ≦ N
    # (Q-P+1)×(S-R+1)≦ 3× 10^5
    # All values in input are integers.

    # 1 ≦ N ≦ 10^{18}
    # 1 ≦ A ≦ N
    # 1 ≦ B ≦ N
    # 1 ≦ P ≦ Q ≦ N
    # 1 ≦

=======
Suggestion 7

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    result = []
    for i in range(P, Q+1):
        row = ''
        for j in range(R, S+1):
            if (i-j) % 2 == 0:
                row += '.'
            else:
                row += '#'
        result.append(row)
    print('\n'.join(result))

=======
Suggestion 8

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())

    # 1 <= N <= 10^18
    # 1 <= A <= N
    # 1 <= B <= N
    # 1 <= P <= Q <= N
    # 1 <= R <= S <= N
    # (Q-P+1) * (S-R+1) <= 3 * 10^5
    # All values in input are integers.

    # 1 <= N <= 10^18
    # 1 <= A <= N
    # 1 <= B <= N
    # 1 <= P <= Q <= N
    # 1 <= R <= S <= N
    # (Q-P+1) * (S-R+1) <= 3 * 10^5
    # All values in input are integers.

    # 1 <= N <= 10^18
    # 1 <= A <= N
    # 1 <= B <= N
    # 1 <= P <= Q <= N
    # 1 <= R <= S <= N
    # (Q-P+1) * (S-R+1) <= 3 * 10^5
    # All values in input are integers.

    # 1 <= N <= 10^18
    # 1 <= A <= N
    # 1 <= B <= N
    # 1 <= P <= Q <= N
    # 1 <= R <= S <= N
    # (Q-P+1) * (S-R+1) <= 3 * 10^5
    # All values in input are integers.

    # 1 <= N <= 10^18
    # 1 <= A <= N
    # 1 <= B <= N
    # 1 <= P <= Q <= N
    # 1 <= R <= S <= N
    # (Q-P+1) * (S-R+1) <= 3 * 10^5
    # All values in input are integers.

    # 1 <= N <= 10^18
    # 1 <= A <= N
    # 1 <= B <= N
    # 1 <= P <= Q <= N
    #

=======
Suggestion 9

def main():
    N,A,B = map(int, input().split())
    P,Q,R,S = map(int, input().split())
    #print(N,A,B,P,Q,R,S)
    print(N,A,B,P,Q,R,S)

=======
Suggestion 10

def find_squares(n,a,b,p,q,r,s):
    if n == 1:
        if a == 1 and b == 1:
            return [1]
        else:
            return [0]
    if a == 1 and b == 1:
        return [1] + [0]*(n-1)
    elif a == 1 and b == n:
        return [0]*(n-1) + [1]
    elif a == n and b == 1:
        return [0]*(n-1) + [1]
    elif a == n and b == n:
        return [1] + [0]*(n-1)
    else:
        if p <= a+b-2 and q >= a+b-2 and r <= a-b+2*n-2 and s >= a-b+2*n-2:
            return [1] + [0]*(n-1)
        elif p <= a+b-2 and q >= a+b-2:
            return [1] + find_squares(n-1,a,b-1,p,q,r,s)
        elif r <= a-b+2*n-2 and s >= a-b+2*n-2:
            return [1] + find_squares(n-1,a-1,b,p,q,r,s)
        else:
            return [0] + find_squares(n-1,a-1,b-1,p,q,r,s)

n,a,b = map(int,input().split())
p,q,r,s = map(int,input().split())
print('\n'.join([''.join([['.','\#'][i] for i in find_squares(n,a,b,p+k,q+k,r+k,s+k)]) for k in range(q-p+1)]))
