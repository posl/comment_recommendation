Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int, input().split())
    if b%a == 0:
        print(int(b/a))
    else:
        print(int(b/a)+1)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A >= B:
        print(1)
    else:
        print(B - A + 1)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if b % a == 0:
        print(b // a)
    else:
        print(b // a + 1)

=======
Suggestion 4

def main():
    #输入
    A, B = map(int, input().split())
    #处理
    #A个插座的电源条可以将一个空插座扩展到A个空插座。
    #所以只要B>A，就可以用一个电源条扩展到B个空插座
    #所以，只要B>A，就需要的电源条数就是1个
    #如果B<=A，那么就需要的电源条数就是B//A+1
    if B<=A:
        ans = 1
    else:
        ans = B//A+1
    #输出
    print(ans)

=======
Suggestion 5

def get_input():
    input = raw_input()
    input = input.split(' ')
    input = map(int, input)
    return input

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if b % a == 0:
        print(b // a)
    else:
        print(b // a + 1)

main()

=======
Suggestion 7

def solve():
    A,B = map(int,input().split())
    print((B-1)//(A-1))

=======
Suggestion 8

def get_power_strips(a, b):
    if b % a == 0:
        return 0
    else:
        return 1
