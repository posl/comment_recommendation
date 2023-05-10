Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    print("Yes" if H <= sum(A) else "No")

main()

=======
Suggestion 2

def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    if h <= sum(a):
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) >= H:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print("Yes" if h <= sum(a) else "No")

=======
Suggestion 5

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) >= H:
        print('Yes')
    else:
        print('No')
main()

=======
Suggestion 6

def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) >= h:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    if h <= sum(a):
        print('Yes')
    else:
        print('No')
    return

=======
Suggestion 8

def main():
    # 標準入力受け取り
    H, N = map(int, input().split())
    A = list(map(int, input().split()))

    # モンスターの体力を減らす
    for i in range(N):
        H -= A[i]

    # モンスターの体力が0以下ならYes
    if H <= 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    H,N = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    if sum(A[0:N-1]) >= H:
        print("Yes")
    else:
        print("No")
