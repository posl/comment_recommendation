Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    q = int(input())
    a = []
    for i in range(q):
        a.append(list(map(int, input().split())))
    ret = []
    bag = []
    for i in range(q):
        if a[i][0] == 1:
            bag.append(a[i][1])
        elif a[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += a[i][1]
        else:
            ret.append(min(bag))
            bag.remove(min(bag))
    for i in range(len(ret)):
        print(ret[i])

=======
Suggestion 2

def main():
    Q = int(input())
    bag = []
    for i in range(Q):
        query = input()
        if query[0] == '1':
            bag.append(int(query.split(' ')[1]))
        elif query[0] == '2':
            for j in range(len(bag)):
                bag[j] += int(query.split(' ')[1])
        else:
            print(min(bag))
            bag.remove(min(bag))
main()

=======
Suggestion 3

def main():
    # 读取输入
    Q = int(input())
    queries = [input().split() for _ in range(Q)]
    #print(queries)
    #print(queries[0])
    #print(queries[0][0])
    #print(queries[0][1])
    #print(queries[0][2])
    #print(queries[0][3])
    #print(queries[0][4])
    #print(queries[0][5])
    #print(queries[0][6])
    #print(queries[0][7])
    #print(queries[0][8])
    #print(queries[0][9])
    #print(queries[0][10])
    #print(queries[0][11])
    #print(queries[0][12])
    #print(queries[0][13])
    #print(queries[0][14])
    #print(queries[0][15])
    #print(queries[0][16])
    #print(queries[0][17])
    #print(queries[0][18])
    #print(queries[0][19])
    #print(queries[0][20])
    #print(queries[0][21])
    #print(queries[0][22])
    #print(queries[0][23])
    #print(queries[0][24])
    #print(queries[0][25])
    #print(queries[0][26])
    #print(queries[0][27])
    #print(queries[0][28])
    #print(queries[0][29])
    #print(queries[0][30])
    #print(queries[0][31])
    #print(queries[0][32])
    #print(queries[0][33])
    #print(queries[0][34])
    #print(queries[0][35])
    #print(queries[0][36])
    #print(queries[0][37])
    #print(queries[0][38])
    #print(queries[0][39])
    #print(queries[0][40])
    #print(queries[0][41])
    #print(queries[0][42])
    #print(queries[0][43])
    #print(queries[0][44])
    #print(queries[0

=======
Suggestion 4

def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int,input().split())))
    bag = []
    for i in range(n):
        if arr[i][0] == 1:
            bag.append(arr[i][1])
        elif arr[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += arr[i][1]
        else:
            print(min(bag))
            bag.remove(min(bag))

=======
Suggestion 5

def main():
    #输入
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(list(map(int,input().split())))

    #处理
    bag = []
    for query in queries:
        if query[0] == 1:
            bag.append(query[1])
        elif query[0] == 2:
            bag = [x+query[1] for x in bag]
        elif query[0] == 3:
            print(min(bag))
            bag.remove(min(bag))

=======
Suggestion 6

def main():
    q = int(input())
    bag = []
    for i in range(q):
        line = input().split()
        if line[0] == "1":
            bag.append(int(line[1]))
        elif line[0] == "2":
            for j in range(len(bag)):
                bag[j] += int(line[1])
        elif line[0] == "3":
            print(min(bag))
            bag.remove(min(bag))

=======
Suggestion 7

def main():
    n = int(input())
    bag = []
    for i in range(n):
        query = input()
        if query[0] == '1':
            bag.append(int(query[2:]))
        elif query[0] == '2':
            for j in range(len(bag)):
                bag[j] += int(query[2:])
        elif query[0] == '3':
            print(min(bag))
            bag.remove(min(bag))

=======
Suggestion 8

def main():
    # 读入数据
    Q = int(input())
    # 初始化一个空的列表
    bag = []
    # 循环Q次
    for i in range(Q):
        # 读入操作类型
        P = int(input())
        # 如果是类型1或2
        if P == 1 or P == 2:
            # 读入整数X
            X = int(input())
            # 如果是类型1
            if P == 1:
                # 把整数X放进袋子里
                bag.append(X)
            # 如果是类型2
            else:
                # 对于袋子里的每个球
                for j in range(len(bag)):
                    # 用该整数加X替换写在上面的整数
                    bag[j] += X
        # 如果是类型3
        else:
            # 找到袋子里整数最小的球
            min_ball = min(bag)
            # 记录写在这个球上的整数
            ans = min_ball
            # 把它扔掉
            bag.remove(min_ball)
            # 打印记录的整数
            print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    nums = []
    for i in range(n):
        num = input().split()
        if num[0] == '1':
            nums.append(int(num[1]))
        elif num[0] == '2':
            nums = [x+int(num[1]) for x in nums]
        elif num[0] == '3':
            print(min(nums))
            nums.remove(min(nums))

=======
Suggestion 10

def main():
    q = int(input())
    op = []
    for i in range(q):
        op.append(list(map(int, input().split())))

    bag = []
    for i in range(q):
        if op[i][0] == 1:
            bag.append(op[i][1])
        elif op[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += op[i][1]
        else:
            bag.sort()
            print(bag[0])
            bag.pop(0)
