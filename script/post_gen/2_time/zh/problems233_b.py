Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    print((y - x) // 10)

=======
Suggestion 2

def main():
    x,y = map(int,input().split())
    if x >= y :
        print(0)
    else:
        print(int((y-x)/10))

=======
Suggestion 3

def main():
    a,b = map(int,input().split())
    if a >= b:
        print(0)
    else:
        print((b-a)//10)
main()
#解答
#在信封上贴的邮票总额为X，还需要贴的邮票总额为Y。
#要使总额达到Y，还需要贴的邮票总额是Y-X。
#因此，答案是（Y-X）/ 10。
#如果（Y-X）/ 10不是整数，则需要再贴一张邮票，因此答案是（Y-X）/ 10 + 1。
#这个问题的关键是，如何将答案的小数部分去除。
#在Python中，可以使用//运算符。例如，如果a和b是整数，则a // b的值是a除以b的商的整数部分。
#如果（Y-X）/ 10不是整数，则（Y-X）// 10 + 1的值是（Y-X）/ 10的整数部分+1。

=======
Suggestion 4

def main():
    x,y = map(int,input().split())
    print((y-x)%10)

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    if x >= y:
        print(0)
    else:
        print((y - x) // 10)

=======
Suggestion 6

def main():
    x, y = map(int, input().split())
    z = y - x
    if z % 10 == 0:
        print(z // 10)
    else:
        print(z // 10 + 1)

=======
Suggestion 7

def solution():
    x, y = map(int, input().split())
    if x >= y:
        print(0)
        return
    else:
        print((y - x) // 10)
        return


solution()
