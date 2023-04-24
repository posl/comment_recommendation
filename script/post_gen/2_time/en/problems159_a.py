Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    print(n * (n - 1) // 2 + m * (m - 1) // 2)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    print(N * (N-1) // 2 + M * (M-1) // 2)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    print((N*(N-1)+M*(M-1))//2)
main()

=======
Suggestion 4

def main():
    #input
    N, M = map(int, input().split())
    #output
    print(N*(N-1)//2 + M*(M-1)//2)
    return

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    print(int(n * (n - 1) / 2 + m * (m - 1) / 2))

main()

If you have any questions, please feel free to ask me.

Thank you very much for reading my article.

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    #N = 0 or 1
    if N == 0:
        print(M)
    #N = 1
    elif N == 1:
        print(M*(M-1)//2)
    #N >= 2
    else:
        print(N*M + (N*(N-1)//2)*(M*(M-1)//2))
