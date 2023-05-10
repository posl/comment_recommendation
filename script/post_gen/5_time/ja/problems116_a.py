Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def triangle_area(a,b,c):
    #直角三角形の面積を求める関数
    #a,b,cはそれぞれ三角形の辺の長さ

    #三辺の長さを昇順に並び替える
    a,b,c = sorted([a,b,c])

    #直角三角形であるか判定
    if a**2 + b**2 == c**2:
        #面積を求める
        area = a*b/2
    else:
        area = 0

    return int(area)

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    print(a*b//2)

=======
Suggestion 3

def main():
    abc = input().rstrip().split(' ')
    ab = int(abc[0])
    bc = int(abc[1])
    ca = int(abc[2])
    print(int(ab * bc / 2))

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    print(int(a*b/2))

=======
Suggestion 5

def main():
    # input
    AB, BC, CA = map(int, input().split())

    # compute
    S = AB * BC // 2

    # output
    print(S)

=======
Suggestion 6

def main():
    #input_lines = input()
    #input_lines = input_lines.split()
    #input_lines = [int(s) for s in input_lines]
    #a = input_lines[0]
    #b = input_lines[1]
    #c = input_lines[2]
    a,b,c = map(int, input().split())
    print(int(a*b/2))

=======
Suggestion 7

def main():
    # n = int(input())
    # a, b = map(int, input().split())
    # s = input()
    a, b, c = map(int, input().split())
    #k = int(input())
    #l = list(map(int, input().split()))
    #l = [list(map(int,input().split())) for i in range(n)]
    #l = [input().split() for i in range(n)]
    #l = [int(input()) for i in range(n)]
    print(int(a*b/2))

=======
Suggestion 8

def main():
    a, b, c = map(int, input().split())
    print(int(a * b / 2))

main()
