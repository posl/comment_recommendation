Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读入数据
    H, A = map(int, input().split())
    # 计算
    print((H + A - 1) // A)

=======
Suggestion 2

def main():
    H,A = map(int,input().split())
    count = 0
    while H > 0:
        H -= A
        count += 1
    print(count)

=======
Suggestion 3

def main():
    H, A = map(int, input().split())
    print((H + A - 1) // A)

=======
Suggestion 4

def main():
    h, a = map(int, input().split())
    ans = 0
    while h > 0:
        h -= a
        ans += 1
    print(ans)

=======
Suggestion 5

def solve():
    H, A = map(int, input().split())
    cnt = 0
    while H > 0:
        H -= A
        cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    H,A = map(int,input().split())
    cnt = 0
    while H > 0:
        H -= A
        cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    H,A = map(int,input().split())
    res = 0
    while H > 0:
        H -= A
        res += 1
    print(res)

=======
Suggestion 8

def main():
    H,A = map(int,input().split())
    #print(H,A)
    count = 0
    while H > 0:
        H -= A
        count += 1
    print(count)

=======
Suggestion 9

def main():
    H, A = map(int, input().split())
    print((H - 1) // A + 1)
