Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    item_list = []
    for i in range(N):
        item_list.append(input())

    print(len(set(item_list)))

=======
Suggestion 2

def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    print(len(s))

=======
Suggestion 3

def main():
    N = int(input())
    S = [input() for i in range(N)]
    print(len(set(S)))

=======
Suggestion 4

def get_count():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    count = 1
    for i in range(1, n):
        if s[i] != s[i-1]:
            count += 1
    return count

=======
Suggestion 5

def count_num():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())

    s_set = set(s)
    return len(s_set)

print(count_num())

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S = set(S)
    print(len(S))

=======
Suggestion 7

def main():
    n=int(input())
    a=[]
    for i in range(n):
        a.append(input())
    print(len(set(a)))

=======
Suggestion 8

def main():
    # 读入
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())

    # 处理
    s = set(s)
    # 输出
    print(len(s))
