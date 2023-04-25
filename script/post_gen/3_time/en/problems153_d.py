Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H = int(input())
    ans = 0
    while H > 0:
        ans += H
        H //= 2
    print(ans)

=======
Suggestion 2

def main():
    H = int(input())
    cnt = 0
    while H > 0:
        H = H // 2
        cnt += 1
    print(2 ** cnt - 1)

=======
Suggestion 3

def main():
    H = int(input())
    ans = 0
    while H > 0:
        ans += H
        H = H // 2
    print(ans)

=======
Suggestion 4

def main():
    H = int(input())
    ans = 1
    while H > 1:
        ans += H
        H //= 2
    print(ans)

=======
Suggestion 5

def main():
    h = int(input())
    ans = 0
    while h > 0:
        h >>= 1
        ans += 1
    print(2 ** ans - 1)

=======
Suggestion 6

def main():
    H = int(input())
    ans = 0
    while H > 0:
        ans += 1
        H >>= 1
    print(ans)

=======
Suggestion 7

def main():
    H = int(input())
    A = [H]
    while True:
        if A[-1] <= 1:
            break
        else:
            A.append(A[-1]//2)
    print(sum(A))

main()

=======
Suggestion 8

def main(h):
    #h = int(input())
    ans = 1
    while h > 1:
        h = h//2
        ans += h
    print(ans)
