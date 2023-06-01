Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, D = map(int, input().split())
    print((N + 2 * D) // (2 * D + 1))

=======
Suggestion 2

def main():
    N, D = map(int, input().split())
    print((N + 2 * D) // (2 * D + 1))

main()

=======
Suggestion 3

def check_apple_tree(n, d):
    if n % (2 * d + 1) == 0:
        return n // (2 * d + 1)
    else:
        return n // (2 * d + 1) + 1

=======
Suggestion 4

def calc_min_checker_num(num_of_trees, distance):
    return num_of_trees // (2 * distance + 1) + 1

=======
Suggestion 5

def main():
    n,d = map(int,input().split())
    print((n+2*d)//(2*d+1))

=======
Suggestion 6

def apple(N, D):
    if N % (2 * D + 1) == 0:
        return N // (2 * D + 1)
    else:
        return N // (2 * D + 1) + 1

=======
Suggestion 7

def main():
    n, d = map(int, input().split())
    print(n // (2 * d + 1) + (1 if n % (2 * d + 1) else 0))

=======
Suggestion 8

def calc_min_checker(tree_num, distance):
    if tree_num < 2:
        return 1
    else:
        return 1 + (tree_num - 2 * distance - 1) // (2 * distance + 1)
