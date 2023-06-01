Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b = map(int, input().split())
    print(100 - (b*100/a))

=======
Suggestion 2

def main():
    print("请输入正常价格和折扣价格：")
    a,b = map(int,input().split())
    print("折扣率为：{:.2f}".format((a-b)/a*100))

main()

=======
Suggestion 3

def get_discount_rate(a, b):
    return (a-b)/a*100

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    print(100 - b * 100 / a)
    return

=======
Suggestion 5

def problem193():
    a,b = map(int, input().split())
    print((a-b)/a*100)

=======
Suggestion 6

def main():
    # A, B = map(int, input().split())
    # print((A-B)*100/A)
    A, B = map(int, input().split())
    print((A-B)*100/A)

=======
Suggestion 7

def problems193_a():
    a,b = map(int,input().split())
    print(100 - b * 100 / a)

problems193_a()

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    print(100 - b / a * 100)

=======
Suggestion 9

def main():
    a, b = map(int, input().split())
    print((a-b)/a*100)

=======
Suggestion 10

def main():
    A,B = map(int,input().split())
    print((A-B)/A*100)
