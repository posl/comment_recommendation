Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    ab, bc, ca = map(int, input().split())
    print(ab * bc // 2)

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    print(a*b//2)

=======
Suggestion 3

def main():
    # 入力
    a, b, c = map(int, input().split())
    # 処理
    ans = a*b//2
    # 出力
    print(ans)

=======
Suggestion 4

def main():
    ab,bc,ca = map(int,input().split())
    print(int(ab*bc/2))

=======
Suggestion 5

def main():
    ab, bc, ca = [int(x) for x in input().split()]
    print(ab * bc // 2)

=======
Suggestion 6

def main():
    # 三角形の辺の長さ
    ab, bc, ca = map(int, input().split())
    # 三角形の面積
    area = (ab * bc) // 2
    print(area)

=======
Suggestion 7

def main():
    #input
    ab, bc, ca = map(int, input().split())
    #output
    print((ab * bc) // 2)

=======
Suggestion 8

def main():
    a,b,c = map(int,input().split())
    print(int((a*b)/2))

=======
Suggestion 9

def main():
    # write your code here
    # use input() to fetch data from STDIN
    # use print() to write your result to STDOUT
    AB,BC,CA = [int(x) for x in input().split()]
    print(int(AB*BC/2))

=======
Suggestion 10

def get_input():
    return map(int, input().split())
