Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c, d, e = map(int, input().split())
    print(5 - len(set([a, b, c, d, e])))

=======
Suggestion 2

def main():
    print(len(set(input().split())))

=======
Suggestion 3

def main():
    a = input().split()
    print(len(set(a)))

=======
Suggestion 4

def main():
    a = list(map(int, input().split()))
    print(len(set(a)))

=======
Suggestion 5

def main():
    a,b,c,d,e = map(int,input().split())
    print(len(set([a,b,c,d,e])))

=======
Suggestion 6

def main():
    a,b,c,d,e = map(int,input().split())
    if a==b==c==d==e:
        print(1)
    elif a==b==c==d or a==b==c==e or a==b==d==e or a==c==d==e or b==c==d==e:
        print(2)
    elif a==b==c or a==b==d or a==b==e or a==c==d or a==c==e or a==d==e or b==c==d or b==c==e or b==d==e or c==d==e:
        print(3)
    else:
        print(5)

=======
Suggestion 7

def main():
    a,b,c,d,e = map(int,input().split())
    nums = [a,b,c,d,e]
    print(len(set(nums)))

=======
Suggestion 8

def main():
    # 读取输入
    a,b,c,d,e = map(int, input().split())
    # 用set去重
    l = [a,b,c,d,e]
    print(len(set(l)))

=======
Suggestion 9

def main():
    # 读入
    input_str = input()
    # 处理
    input_list = input_str.split(" ")
    input_list = list(map(int, input_list))
    input_set = set(input_list)
    # 输出
    print(len(input_set))

=======
Suggestion 10

def main():
    s = input()
    num_list = s.split()
    num_set = set(num_list)
    print(len(num_set))
