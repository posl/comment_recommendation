Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_distinct_num(list):
    return len(set(list))

=======
Suggestion 2

def main():
    a, b, c, d, e = map(int, input().split())
    list = [a, b, c, d, e]
    print(len(set(list)))

=======
Suggestion 3

def main():
    a,b,c,d,e = map(int,input().split())
    print(len(set([a,b,c,d,e])))

=======
Suggestion 4

def main():
    input_str = input()
    input_list = input_str.split()
    input_list = list(map(int, input_list))
    input_list = set(input_list)
    print(len(input_list))

=======
Suggestion 5

def main():
    #print("请输入五个整数：")
    num = input()
    num_list = num.split()
    num_set = set(num_list)
    print(len(num_set))

=======
Suggestion 6

def main():
    a,b,c,d,e = map(int, input().split())
    print(len({a,b,c,d,e}))

=======
Suggestion 7

def main():
    # 读取输入
    nums = input().split()
    # 去重
    nums = set(nums)
    # 打印输出
    print(len(nums))

=======
Suggestion 8

def main():
    a = [int(i) for i in input().split()]
    a.sort()
    res = 1
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            res += 1
    print(res)

=======
Suggestion 9

def main():
    list = input().split()
    print(len(set(list)))
