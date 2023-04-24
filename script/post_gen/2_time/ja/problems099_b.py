Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    n = b - a - 1
    x = n * (n + 1) // 2
    print(x - a)

main()

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print((b-a)*(b-a+1)//2-b)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print(b-a-1)

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    print(b-a-1)

main()

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print((b-a)*(b+a-1)//2 - a)

=======
Suggestion 6

def main():
    a,b = input().split()
    a = int(a)
    b = int(b)
    if a == b:
        print(0)
    else:
        print(b-a-1)

=======
Suggestion 7

def snow(a, b):
    # 雪の積もり具合を求める
    # 雪が積もっていない場合は 0 を返す
    if a == b:
        return 0
    else:
        # 雪が積もっている場合は積もり具合を返す
        # 雪が積もっている場合は、
        # 1. 2 つの塔の高さの差を求める
        # 2. 2 つの塔の高さの差が偶数か奇数かで場合分けを行う
        # 3. 奇数の場合は、雪が積もっている塔の高さの差の半分を返す
        # 4. 偶数の場合は、雪が積もっている塔の高さの差の半分 - 1 を返す
        # 5. ただし、雪が積もっている塔の高さの差が 1 の場合は 0 を返す
        diff = b - a
        if diff % 2 == 0:
            return diff // 2 - 1
        else:
            return diff // 2
