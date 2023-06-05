Synthesizing 10/10 solutions

=======
Suggestion 1

def add_to_bag(bag, x):
    if len(bag) == 0:
        bag.append(x)
    else:
        bag.append(x + bag[-1])

=======
Suggestion 2

def main():
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(input().split())
    result = []
    bag = []
    for query in queries:
        if query[0] == '1':
            bag.append(int(query[1]))
        elif query[0] == '2':
            for i in range(len(bag)):
                bag[i] += int(query[1])
        else:
            min_num = min(bag)
            result.append(min_num)
            bag.remove(min_num)
    for i in result:
        print(i)

=======
Suggestion 3

def main():
    n = int(input())
    bag = []
    for i in range(n):
        query = input().split()
        if query[0] == '1':
            bag.append(int(query[1]))
        elif query[0] == '2':
            for i in range(len(bag)):
                bag[i] += int(query[1])
        elif query[0] == '3':
            print(min(bag))
            bag.remove(min(bag))

=======
Suggestion 4

def main():
    # 读入数据
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))
    # print(data)

    # 定义一个空列表，用于存储最终的输出结果
    result = []

    # 定义一个空列表，用于存储袋子里的球
    bag = []

    # 循环读取每一行数据
    for i in range(n):
        # 判断当前行的第一个数字是1, 2, 还是3
        if data[i][0] == 1:
            # 如果是1，则在袋子里放入一个新的球
            bag.append(data[i][1])
        elif data[i][0] == 2:
            # 如果是2，则将袋子里的每个球的数字都加上当前行的第二个数字
            for j in range(len(bag)):
                bag[j] += data[i][1]
        elif data[i][0] == 3:
            # 如果是3，则将袋子里的最小的数字取出来
            # 并将取出来的数字放入result列表中
            # 并从袋子里删除这个数字
            result.append(min(bag))
            bag.remove(min(bag))
    # print(result)

    # 循环输出result列表中的数字
    for i in range(len(result)):
        print(result[i])

=======
Suggestion 5

def main():
    n = int(input())
    q = [int(input()) for i in range(n)]
    s = []
    for i in range(n):
        if q[i] == 3:
            print(s[0])
            del s[0]
        else:
            if q[i] == 1:
                s.append(q[i+1])
            else:
                s = [j+q[i+1] for j in s]

=======
Suggestion 6

def main():
    # 读取输入
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]

    # 用来记录结果
    result = []

    # 用来记录最小值
    min_value = 0

    # 用来记录最小值的个数
    min_value_count = 0

    # 用来记录最小值的和
    min_value_sum = 0

    # 用来记录最小值的平均值
    min_value_average = 0

    for i in range(Q):
        if query[i][0] == 1:
            # 如果是类型1，把整数放进袋子里
            min_value = min(query[i][1], min_value)
            min_value_count += 1
            min_value_sum += query[i][1]
            min_value_average = min_value_sum / min_value_count
        elif query[i][0] == 2:
            # 如果是类型2，对于袋子里的每个球，用该整数加X_i替换写在上面的整数
            min_value = min(query[i][1] + min_value, min_value)
            min_value_sum += query[i][1] * min_value_count
            min_value_average = min_value_sum / min_value_count
        else:
            # 如果是类型3，拿起袋子里整数最小的球（如果有多个这样的球，拿起其中一个）。记录写在这个球上的整数并把它扔掉。
            result.append(min_value)
            min_value_count -= 1
            min_value_sum -= min_value
            if min_value_count > 0:
                min_value_average = min_value_sum / min_value_count
            else:
                min_value_average = 0

    # 输出结果
    for i in range(len(result)):
        print(result[i])

=======
Suggestion 7

def main():
    q = int(input())
    query_list = []
    for i in range(q):
        query_list.append(input().split())

    bag = []
    for i in range(q):
        if query_list[i][0] == '1':
            bag.append(int(query_list[i][1]))
        elif query_list[i][0] == '2':
            for j in range(len(bag)):
                bag[j] += int(query_list[i][1])
        else:
            min = bag[0]
            for j in range(len(bag)):
                if min > bag[j]:
                    min = bag[j]
            print(min)
            bag.remove(min)

=======
Suggestion 8

def main():
    from sys import stdin
    from heapq import heapify, heappop, heappush
    input = stdin.readline
    q = int(input())
    q1 = []
    q2 = []
    q2_sum = 0
    for _ in range(q):
        p, x = map(int, input().split())
        if p == 1:
            heappush(q1, x)
            q2_sum += x
        elif p == 2:
            heappush(q2, x)
            q2_sum += x
            if len(q2) > len(q1):
                q2_sum -= heappop(q2)
        else:
            print(q1[0], q2_sum)
            if len(q2) > len(q1):
                q2_sum -= heappop(q2)
            heappop(q1)
main()

=======
Suggestion 9

def main():
    n = int(input())
    q = []
    for i in range(n):
        q.append(input().split())

    bag = []
    for i in range(n):
        if q[i][0] == '1':
            bag.append(int(q[i][1]))
        elif q[i][0] == '2':
            for j in range(len(bag)):
                bag[j] += int(q[i][1])
        elif q[i][0] == '3':
            bag.sort()
            print(bag[0])
            bag.pop(0)

=======
Suggestion 10

def main():
    # 读入数据
    n = int(input())
    queries = []
    for _ in range(n):
        queries.append(list(map(int, input().split())))

    # 处理
    bag = []
    for i in range(n):
        if queries[i][0] == 1:
            bag.append(queries[i][1])
        elif queries[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += queries[i][1]
        elif queries[i][0] == 3:
            print(min(bag))
            bag.remove(min(bag))
