Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    print('Yes' if n == m else 'No')

=======
Suggestion 2

def main():
    n,m = map(int, input().split())
    if n == m:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    if N == M:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    if N == M:
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 5

def problem152_a():
    N, M = input().split()
    N = int(N)
    M = int(M)
    if M == N:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def get_input():
    input_str = input("请输入N和M：")
    input_list = input_str.split()
    return input_list
