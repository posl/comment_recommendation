Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def check_apple_tree(n, d):
    if n % (2 * d + 1) == 0:
        return n // (2 * d + 1)
    else:
        return n // (2 * d + 1) + 1

=======
Suggestion 2

def solution(N, D):
    if N == 1:
        return 1
    if D == 1:
        return N

    count = 0
    while N > 0:
        count += 1
        N = N - (2 * D + 1)
    return count

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    print((N + 2 * D) // (2 * D + 1))

=======
Suggestion 4

def main():
    n,d = map(int,input().split())
    print(2 if n % (2 * d + 1) == 0 else n // (2 * d + 1) + 1)

=======
Suggestion 5

def main():
    n, d = map(int, input().split())
    print(int(n/(2*d+1))+1 if n%(2*d+1) != 0 else int(n/(2*d+1)))

=======
Suggestion 6

def main():
    n, d = map(int, input().split())
    print(n // (2*d + 1) + (1 if n % (2*d + 1) > 0 else 0))

=======
Suggestion 7

def main():
    n, d = map(int, input().split())
    print(int((n+(2*d))/(2*d+1)))

=======
Suggestion 8

def main():
    N, D = map(int, input().split())
    print(int((N+2*D)/(2*D+1)))

=======
Suggestion 9

def main():
    # 读取数据
    n, d = map(int, input().split())
    # 计算结果
    print((n + 2 * d) // (2 * d + 1))
