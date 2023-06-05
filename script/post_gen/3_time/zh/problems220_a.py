Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 2

def main():
    # 读取输入
    a, b, c = map(int, input().split())

    # 计算答案
    answer = -1
    for i in range(a, b + 1):
        if i % c == 0:
            answer = i
            break

    # 输出
    print(answer)

=======
Suggestion 3

def main():
    a,b,c = map(int, input().split())
    for i in range(a,b+1):
        if i%c == 0:
            print(i)
            exit()
    print(-1)

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    for i in range(A, B+1):
        if i % C == 0:
            print(i)
            return
    print(-1)
