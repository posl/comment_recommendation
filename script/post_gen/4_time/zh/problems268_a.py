Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    nums = input().split()
    nums = [int(i) for i in nums]
    print(len(set(nums)))

=======
Suggestion 2

def main():
    A, B, C, D, E = map(int, input().split())
    print(len(set([A, B, C, D, E])))

=======
Suggestion 3

def main():
    # 将输入的五个整数存入列表
    a = list(map(int, input().split()))
    # 将列表转换为集合，集合中的元素不重复
    b = set(a)
    # 打印集合的长度
    print(len(b))

=======
Suggestion 4

def main():
    nums = list(map(int, input().split()))
    print(len(set(nums)))

=======
Suggestion 5

def main():
    num = [int(i) for i in input().split()]
    print(len(set(num)))

=======
Suggestion 6

def main():
    a, b, c, d, e = map(int, input().split())
    A = [a, b, c, d, e]
    print(len(set(A)))
main()

=======
Suggestion 7

def main():
    # 读取输入
    input_str = input()
    str_list = input_str.split(' ')
    int_list = [int(str) for str in str_list]
    # 去重
    int_set = set(int_list)
    # 输出
    print(len(int_set))

=======
Suggestion 8

def main():
    a,b,c,d,e = map(int, input().split())
    print(len(set([a,b,c,d,e])))

=======
Suggestion 9

def main():
    # 读取输入
    int_list = list(map(int, input().split()))
    # 用set去重
    int_set = set(int_list)
    # 打印答案
    print(len(int_set))

=======
Suggestion 10

def main():
    # 读取输入
    a, b, c, d, e = map(int, input().split())
    # 用集合去重
    print(len(set([a, b, c, d, e])))
