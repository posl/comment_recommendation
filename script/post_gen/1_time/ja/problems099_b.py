Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print((b * (b + 1) // 2) - (a * (a + 1) // 2))

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print((b - a) * (b - a + 1) // 2 - (b - a))

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print((b-a)*(b-a+1)//2-b)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    print((b-a)*(b-a+1)//2 - (b-a+1))

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    x = b - a - 1
    print(x*(x+1)//2 - a)

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    # どの塔の高さが大きいかを判定する
    if a > b:
        a, b = b, a
    # 2 つの塔の高さを求める
    a_height = (a + 1) * a // 2
    b_height = (b + 1) * b // 2
    # 2 つの塔の高さの差を求める
    height = b_height - a_height
    # 2 つの塔の高さの差を出力する
    print(height)

=======
Suggestion 7

def main():

    a,b = map(int,input().split())

    #h = 1
    #for i in range(1,a+1):
    #    h += i
    #h2 = 1
    #for i in range(1,b+1):
    #    h2 += i
    #print(h2-h)

    h = 0
    for i in range(1,a+1):
        h += i
    h2 = 0
    for i in range(1,b+1):
        h2 += i
    print(h2-h)
